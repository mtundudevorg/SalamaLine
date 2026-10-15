from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.seed_role import seed_role


router=APIRouter(tags=["Seeed"])


@router.post("/seed")
def seed(db:Session=Depends(get_db)):
    return seed_role(db)