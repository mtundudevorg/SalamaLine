from jose import jwt,JWTError
from app.core.config import settings
from datetime import datetime,timedelta
from fastapi import HTTPException,status
from pwdlib import PasswordHash

Hash=PasswordHash.recommended()




def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now() + timedelta(minutes=settings.EXPIRE_ACCESS_TOKEN)
    
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    return token


def decode_token(token:str):
    try:
        paylod=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        user_id=paylod.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="token has no user details")
        return paylod
    except JWTError:
        return None
    


class hashing:
    @staticmethod
    def hash_password(password):
        return Hash.hash(password)
    @staticmethod
    def verify_password(plain_password,hashed_password):
        return Hash.verify(plain_password,hashed_password)    
    