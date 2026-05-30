import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

def create_structured_view():
    load_dotenv()
    
    base_url = os.environ.get("DBREPO_BASE_URL", "https://test.dbrepo.tuwien.ac.at").rstrip("/")
    database_id = os.environ.get("DBREPO_DATABASE_ID", "ed890fa1-154c-4a66-8529-4088c97f68db")
    
    username = os.environ.get("TU_USERNAME") or os.environ.get("DBREPO_USERNAME")
    password = os.environ.get("TU_PASSWORD") or os.environ.get("DBREPO_PASSWORD")
    
    if not username or not password:
        print("Please provide TU_USERNAME and TU_PASSWORD environment variables.")
        return

    auth = HTTPBasicAuth(username, password)
    headers = {"Content-Type": "application/json"}

    print("1. Fetching tables to resolve UUIDs...")
    tables_resp = requests.get(f"{base_url}/api/v1/database/{database_id}/table", auth=auth)
    tables_resp.raise_for_status()
    table_map = {t["name"]: t["id"] for t in tables_resp.json()}
    
    print("2. Fetching columns for required tables...")
    col_map = {}
    required_tables = ["measurements", "sampling_points", "pollutants", "validity_flags", "verification_flags"]
    for t_name in required_tables:
        t_id = table_map[t_name]
        table_resp = requests.get(f"{base_url}/api/v1/database/{database_id}/table/{t_id}", auth=auth)
        table_resp.raise_for_status()
        col_map[t_name] = {c["name"]: c["id"] for c in table_resp.json().get("columns", [])}

    # 3. Construct the JSON payload corresponding to the API documentation schema
    # Note: Complex operations like CASE WHEN and EXTRACT are omitted as they are not 
    # supported by the structured query JSON format. Feature engineering is instead 
    # handled client-side in your ingest_dbrepo.py pipeline.
    payload = {
        "name": "view_no2_classification_features",
        "is_public": True,
        "is_schema_public": True,
        "query": {
            "datasource_ids": [table_map["measurements"]],
            "columns": [
                {"id": col_map["measurements"]["measurement_id"], "alias": "measurement_id"},
                {"id": col_map["measurements"]["start_time"], "alias": "start_time"},
                {"id": col_map["measurements"]["value"], "alias": "value"},
                {"id": col_map["measurements"].get("data_capture"), "alias": "data_capture"},
                {"id": col_map["validity_flags"]["validity_code"], "alias": "validity"},
                {"id": col_map["verification_flags"]["verification_code"], "alias": "verification"},
                {"id": col_map["sampling_points"]["sampling_point_code"], "alias": "samplingpoint"}
            ],
            "joins": [
                {
                    "type": "inner",
                    "datasource_id": table_map["sampling_points"],
                    "conditionals": [{
                        "column_id": col_map["measurements"]["sampling_point_id"],
                        "foreign_column_id": col_map["sampling_points"]["sampling_point_id"]
                    }]
                },
                {
                    "type": "inner",
                    "datasource_id": table_map["pollutants"],
                    "conditionals": [{
                        "column_id": col_map["measurements"]["pollutant_id"],
                        "foreign_column_id": col_map["pollutants"]["pollutant_id"]
                    }]
                },
                {
                    "type": "inner",
                    "datasource_id": table_map["validity_flags"],
                    "conditionals": [{
                        "column_id": col_map["measurements"]["validity_id"],
                        "foreign_column_id": col_map["validity_flags"]["validity_id"]
                    }]
                },
                {
                    "type": "inner",
                    "datasource_id": table_map["verification_flags"],
                    "conditionals": [{
                        "column_id": col_map["measurements"]["verification_id"],
                        "foreign_column_id": col_map["verification_flags"]["verification_id"]
                    }]
                }
            ],
            "filters": [],
            "orders": []
        }
    }
    
    # Strip out any potential None column lookups (like data_capture if missing)
    payload["query"]["columns"] = [c for c in payload["query"]["columns"] if c["id"] is not None]

    # We skip trying to fetch and add the '=' operator for the pollutant filter 
    # because the DBRepo database inventory verifies the DB only contains 'NO2' rows anyway.

    print("3. Creating view 'view_no2_classification_features' via structured API...")
    view_url = f"{base_url}/api/v1/database/{database_id}/view"
    
    response = requests.post(view_url, json=payload, auth=auth, headers=headers)
    
    if response.status_code in [200, 201, 202]:
        print(" -> Successfully created view!")
    elif response.status_code == 409:
        print(" -> View already exists.")
    else:
        print(f" -> Failed to create view: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    create_structured_view()