from sqlalchemy.orm import Session
from app.models.user import User
from app.models.role import Role
from app.models.roleuser import RoleUser
from app.schemas.user import UserCeate
from sqlalchemy import or_
from app.core.security import hashing,create_access_token
from fastapi import HTTPException,status

def login_user(username:str,password:str,db:Session):
    user=db.query(User).filter(or_(
                                User.email==username,
                                User.Phone==username)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong email ot password")
    if not (hashing.verify_password(password,user.password)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="wrong email or password")
    
    token=create_access_token({"sub":str(user.id)})
    
    return{
        "access_token":token,
        "token_type":"Bearer"
    }


    
def usercreate(db:Session,data:UserCeate):
    existing_user=db.query(User).filter(User.email==data.email and User.Phone==data.Phone).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="already have an account")
    if not data.email and data.phone:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="one or both email or phone number is required")
    
    user=User(
        full_name=data.full_name,
        password=hashing.hash_password(data.password),
        Phone=data.Phone,
        email=data.email,
        is_active=True
        
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    role=db.query(Role).filter(Role.name=="user").first()
    
    
    roleuser=RoleUser(
        user_id=user.id,
        role_id=role.id
    )

    db.add(roleuser)
    db.commit()
    
    
    return user
    
     