from fastapi import FastAPI
from app.core.config import settings


app=FastAPI(title=settings.APP_NAME)




@app.get("/health",tags=["Health"])
def health():
    return {
        "status":"Ok",
        "message":"Welcome to SalamaLine Platform"
    }