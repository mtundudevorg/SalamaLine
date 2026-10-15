from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hashing,create_access_token
from fastapi import HTTPException,status

def login_user(email:str,password:str,db:Session):
    user=db.query(User).filter(User.email==email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong email ot password")
    if not (hashing.verify_password(password,user.password)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong email or password")
    
    token=create_access_token({"sub":user.id})
    
    return{
        "access_token":token,
        "token_type":"Bearer"
    }