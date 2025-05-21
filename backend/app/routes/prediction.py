
from fastapi import APIRouter

router = APIRouter()

@router.get("/attrition")
def predict_attrition():
    return {"prediction": "Attrition forecast will be implemented here"}

@router.get("/cost_forecast")
def predict_cost():
    return {"forecast": "Manpower cost forecast will be implemented here"}
