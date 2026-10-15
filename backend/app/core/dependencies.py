from sqlalchemy.orm import Session
from app.core.security import decode_token
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from app.models.user import User
from app.core.database import get_db
from app.models.roleuser import RoleUser
from app.models.role import Role
from app.models.user import User


oauth2_schema=OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(db:Session=Depends(get_db),token:str=Depends(oauth2_schema)):
    payload=decode_token(token)
    user_id=payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid or expire token")
    user=db.query(User).filter(User.id==user_id).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="user account is not active")
    
    return user


def role_required(required_role:str):
    def role_check(db:Session=Depends(get_db),
                     current_user:User=Depends(get_current_user)):
        roles=db.query(RoleUser).join(RoleUser,RoleUser.role_id==Role.id).filter(RoleUser.user_id==current_user.id).all()
        role_name={role.name for role in roles}
        if "admin" in role_name:
            return current_user
        
        if required_role not in role_name:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid Role")
        
        return current_user
    return role_check
        
    
