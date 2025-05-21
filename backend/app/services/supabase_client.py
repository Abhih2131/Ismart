import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_TABLE = os.getenv("SUPABASE_TABLE")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_all_employees():
    try:
        response = supabase.table(SUPABASE_TABLE).select("*").execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}
