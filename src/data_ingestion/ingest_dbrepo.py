import os
import requests
import pandas as pd

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

DBREPO_BASE_URL = os.environ.get(
    "DBREPO_BASE_URL", 
    "https://test.dbrepo.tuwien.ac.at"
)
DATABASE_ID = os.environ.get("DBREPO_DATABASE_ID", "ed890fa1-154c-4a66-8529-4088c97f68db")
VIEW_DATA_PATH_TEMPLATE = os.environ.get(
    "DBREPO_VIEW_DATA_PATH_TEMPLATE",
    "/api/v1/database/{database_id}/view/{view_name}/data"
)


def fetch_view_data(view_name: str) -> pd.DataFrame:
    """
    Fetches data from a specific DBRepo SQL view using the REST API.
    Includes robust error handling as required by T2.6.
    """
    endpoint = VIEW_DATA_PATH_TEMPLATE.format(
        database_id=DATABASE_ID,
        view_name=view_name,
    )
    url = f"{DBREPO_BASE_URL.rstrip('/')}{endpoint}"
    
    headers = {"Accept": "application/json"}
    token = os.environ.get("DBREPO_API_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    print(f"Fetching data from {url}...")
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        
        data = response.json()
        if isinstance(data, dict):
            data = data.get("data", data.get("rows", data.get("content", data)))
        df = pd.DataFrame(data)
        print(f"Successfully loaded {len(df)} rows from {view_name}.")
        return df
        
    except requests.exceptions.ConnectionError as e:
        raise RuntimeError(f"Connection error: Failed to connect to DBRepo while fetching '{view_name}'. Check your network or the URL: {e}")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"HTTP error: Unexpected response code for view '{view_name}': {e}")
    except requests.exceptions.Timeout as e:
        raise RuntimeError(f"Timeout error: The request timed out while fetching view '{view_name}': {e}")
    except ValueError as e:
        raise RuntimeError(f"Parse error: Failed to decode JSON response for view '{view_name}'. The API may have returned an unexpected format: {e}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An unexpected request error occurred for view '{view_name}': {e}")


if __name__ == "__main__":
    features_df = fetch_view_data("view_no2_classification_features")
    balanced_df = fetch_view_data("view_balanced_pollution_samples")
    
    print("\n--- SUCCESS! DATA PIPELINE IS LIVE ---")
    print(features_df.head())
