
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_employees():
    return {"message": "List of employees from Supabase will be here"}
