from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from contextlib import asynccontextmanager


from app.api.routers import user_router,auth_router,seed,verification

@asynccontextmanager
async def lifespan(app:FastAPI):
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("Ok\nHealthly\nDATABASE CONNECTED SUCCESSFULLY")
    except SQLAlchemyError as Error:             
        print(f"❌DATABASE CONNECTION FAILED :{Error}")
        
    yield    
    
    
app=FastAPI(title=settings.APP_NAME,
            version=settings.VERSION,
            debug=settings.DEBUG,
            description=settings.DESCRIPTION,
            lifespan=lifespan)

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(verification.router)
app.include_router(seed.router)


@app.get("/health",tags=["Health"])
def health():
    return {
        "status":"Ok",
        "message":"Welcome to SalamaLine Platform"
    }

