from dotenv import load_dotenv
load_dotenv()

from fastapi import APIRouter, HTTPException
from supabase import create_client, Client
import os

router = APIRouter()

# Initialize Supabase client using environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_TABLE = os.getenv("SUPABASE_TABLE")

if not all([SUPABASE_URL, SUPABASE_KEY, SUPABASE_TABLE]):
    raise ValueError("Missing Supabase environment variables")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@router.get("/employees")
def get_employees():
    try:
        response = supabase.table(SUPABASE_TABLE).select("*").execute()
        if response.error:
            raise HTTPException(status_code=500, detail=str(response.error))
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
