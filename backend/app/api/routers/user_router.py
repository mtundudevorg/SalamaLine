from fastapi import APIRouter,Depends,Query
from app.schemas.user import UserCeate,UserResponse,UserUpdate,PaginationResponse
from app.services.user_sevices import USerServices
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import desc
from app.models.user import User
from app.core.dependencies import get_current_user


router=APIRouter(tags=["User managments"],prefix="/user")



@router.post("/",response_model=UserResponse)
def create_user(data:UserCeate,db:Session=Depends(get_db)):
    return USerServices.usercreate(db,data)

@router.get("/",response_model=PaginationResponse)
def all_user(search:str=None,
             page:int=Query(1,ge=1),
             limit:int=Query(10,ge=10,le=100),
             sort:str=None,
             db:Session=Depends(get_db)):
    return USerServices.all_user(db,page,limit,sort,search)

@router.get("/user",response_model=UserResponse)
def single_user(user_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return USerServices.single_user(db,user_id)

@router.put("/",response_model=UserResponse)
def user_update(user_id:int,data:UserUpdate,db:Session=Depends(get_db)):
    return USerServices.update_user(db,data,user_id)


@router.delete("/")
def delete_user(user_id:int,db:Session=Depends(get_db)):
    return USerServices.delete_user(db,user_id)