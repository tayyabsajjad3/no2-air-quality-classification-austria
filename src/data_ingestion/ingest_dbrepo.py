import os
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
    

DBREPO_BASE_URL = os.environ.get(
    "DBREPO_BASE_URL", 
    "https://test.dbrepo.tuwien.ac.at"
)
DATABASE_ID = os.environ.get("DBREPO_DATABASE_ID", "ed890fa1-154c-4a66-8529-4088c97f68db")
DBREPO_TOKEN = os.environ.get("DBREPO_TOKEN")

TABLE_IDS = {
    "measurements": "0082a413-69b5-40a3-ac29-a7243961312d",
    "sampling_points": "b277e2ed-1fab-4ac3-962b-b1e82026ae5e",
    "validity_flags": "4b62c1b0-295b-4697-8c91-f61f075c8348",
    "verification_flags": "2e096722-778b-4f12-a236-5f32ad9556e4"
}

def fetch_table_data(table_name: str) -> pd.DataFrame:
    """Fetches raw table data directly from DBRepo."""
    table_id = TABLE_IDS[table_name]
    base_url = f"{DBREPO_BASE_URL.rstrip('/')}/api/v1/database/{DATABASE_ID}/table/{table_id}/data"
    
    headers = {"Accept": "application/json"}
    
    username = os.environ.get("TU_USERNAME") or os.environ.get("DBREPO_USERNAME")
    password = os.environ.get("TU_PASSWORD") or os.environ.get("DBREPO_PASSWORD")
    
    auth_creds = HTTPBasicAuth(username, password) if username and password else None

    print(f"Fetching table '{table_name}' from DBRepo API...")
    all_data = []
    page = 0
    size = 10000  # Safe pagination size to avoid 400 errors
    
    try:
        while True:
            url = f"{base_url}?page={page}&size={size}"
            response = requests.get(url, headers=headers, timeout=60, auth=auth_creds)
            response.raise_for_status()
            
            chunk = response.json()
            if not chunk:
                break
                
            all_data.extend(chunk)
            if len(chunk) < size:
                break
                
            page += 1
        return pd.DataFrame(all_data)
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"HTTP error fetching {table_name}: {e.response.status_code} - {e.response.text}") from e
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error fetching {table_name}: {e}") from e

def fetch_view_data(view_name: str) -> pd.DataFrame:
    """
    Fetches data from DBRepo REST API. 
    Since DBRepo view creation requires DB owner permissions, this safely 
    fetches the base public tables and replicates the view logic in Pandas.
    """
    try:
        if view_name == "view_no2_classification_features":
            m = fetch_table_data("measurements")
            sp = fetch_table_data("sampling_points")
            val = fetch_table_data("validity_flags")
            ver = fetch_table_data("verification_flags")
            
            df = m.merge(sp[['sampling_point_id', 'sampling_point_code']], on='sampling_point_id', how='left')
            df = df.merge(val[['validity_id', 'validity_code']], on='validity_id', how='left')
            df = df.merge(ver[['verification_id', 'verification_code']], on='verification_id', how='left')
            
            df['start_time'] = pd.to_datetime(df['start_time'])
            df['month'] = df['start_time'].dt.month
            df['hour'] = df['start_time'].dt.hour
            df['weekday'] = df['start_time'].dt.weekday
            
            df['value'] = pd.to_numeric(df['value'])
            df['target_elevated_no2'] = (df['value'] >= 40).astype(int)
            
            if 'data_capture' not in df.columns:
                df['data_capture'] = pd.NA
            df['data_capture_missing'] = df['data_capture'].isna().astype(int)
            
            df = df.rename(columns={
                'sampling_point_code': 'samplingpoint',
                'validity_code': 'validity',
                'verification_code': 'verification'
            })
            print(f"Successfully constructed {len(df)} rows for {view_name}.")
            return df
        else:
            raise ValueError(f"Unknown view replication requested: {view_name}")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data from DBRepo API: {e}")

if __name__ == "__main__":
    features_df = fetch_view_data("view_no2_classification_features")
    print("\n--- SUCCESS! DATA PIPELINE IS LIVE ---")
    print(features_df.head())