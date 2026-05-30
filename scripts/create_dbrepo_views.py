import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

ROOT = Path(__file__).resolve().parents[1]
VIEWS_FILE = ROOT / "docs" / "views.sql"

ENDPOINT = "https://test.dbrepo.tuwien.ac.at"
DATABASE_ID = "ed890fa1-154c-4a66-8529-4088c97f68db"

def get_auth_token():
    """Authenticates and retrieves an access token if credentials are provided."""
    username = os.getenv("TU_USERNAME")
    password = os.getenv("TU_PASSWORD")
    
    if not username or not password:
        print("No TU_USERNAME/TU_PASSWORD found. Attempting creation without token...")
        return None
        
    # NOTE: In DBRepo 1.13, you typically authenticate via Keycloak or via basic auth headers 
    # depending on instance setup. If you already have a static DBREPO_TOKEN, return that:
    if "DBREPO_TOKEN" in os.environ:
        return os.environ["DBREPO_TOKEN"]
        
    print("Please export DBREPO_TOKEN in your environment or use the DBRepo web UI.")
    return None

def create_views():
    load_dotenv(ROOT / ".env")
    # token = get_auth_token()
    
    headers = {"Content-Type": "application/json"}
    # if token:
    #     headers["Authorization"] = f"Bearer {token}"

    username = os.environ.get("TU_USERNAME") or os.environ.get("DBREPO_USERNAME")
    password = os.environ.get("TU_PASSWORD") or os.environ.get("DBREPO_PASSWORD")
    
    auth_creds = HTTPBasicAuth(username, password) if username and password else None


    # Split the views.sql file into individual CREATE VIEW statements
    sql_text = VIEWS_FILE.read_text(encoding="utf-8")
    statements = [stmt.strip() for stmt in sql_text.split(";") if "CREATE VIEW" in stmt.upper()]
    
    api_url = f"{ENDPOINT}/api/v1/database/{DATABASE_ID}/view"
    
    for stmt in statements:
        # Extract the view name directly from the statement
        view_name = [word for word in stmt.split() if "view_" in word.lower()][0]
        
        payload = {
            "name": view_name,
            "query": stmt,
            "is_public": True
        }
        
        print(f"Creating view: {view_name}...")
        response = requests.post(api_url, json=payload, headers=headers, auth=auth_creds)
        
        if response.status_code in [200, 201, 202]:
            print(f" -> Successfully created {view_name}!")
        elif response.status_code == 409:
            print(f" -> View {view_name} already exists.")
        else:
            print(f" -> Failed to create {view_name}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    create_views()