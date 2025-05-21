from fastapi import APIRouter
from app.services.supabase_client import fetch_all_employees

router = APIRouter()

@router.get("/")
def get_employees():
    return fetch_all_employees()
