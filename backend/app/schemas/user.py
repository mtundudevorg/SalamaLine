from pydantic import BaseModel,EmailStr,ConfigDict
from typing import Optional,List
from datetime import datetime



class UserCeate(BaseModel):
    full_name:str
    email:Optional[EmailStr]=None
    password:str
    Phone:Optional[str]=None
    
class UserUpdate(BaseModel):
    full_name:str
    email:Optional[EmailStr]=None
    Phone:Optional[str]=None
        

class UserResponse(BaseModel):
    id:int
    full_name:str
    email:Optional[EmailStr]=None
    Phone:Optional[str]=None
    is_active:bool
    created_at:datetime
    updated_at:datetime
    

class PaginationResponse(BaseModel):
    Pagination:dict
    user: List[UserResponse] 
    
    model_config=ConfigDict(
        from_attributes=True
    )