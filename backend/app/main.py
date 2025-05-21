
from fastapi import FastAPI
from app.routes import employees, prediction

app = FastAPI()

app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(prediction.router, prefix="/prediction", tags=["Prediction"])

@app.get("/")
def root():
    return {"message": "Welcome to Ismart API"}
