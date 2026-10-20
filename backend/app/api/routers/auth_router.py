from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.user import UserCeate,UserResponse
from app.core.database import get_db
from app.services.auth_service import login_user,usercreate



router=APIRouter(tags=["Authorization"])

@router.post("/register",response_model=UserResponse)
def create_user(data:UserCeate,db:Session=Depends(get_db)):
    return usercreate(db,data)

@router.post("/login")
def login(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return login_user(data.username,data.password,db)