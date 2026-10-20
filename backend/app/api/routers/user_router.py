from fastapi import APIRouter,Depends,Query
from app.schemas.user import UserCeate,UserResponse,UserUpdate,PaginationResponse
from app.services.user_sevices import USerServices
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import desc
from app.models.user import User
from app.core.dependencies import get_current_user,role_required

admin_required=role_required(["admin"])
user_required=role_required(["admin","user","provider"])


router=APIRouter(tags=["User managments"],prefix="/user")


@router.get("/",response_model=PaginationResponse)
def all_user(search:str=None,
             page:int=Query(1,ge=1),
             limit:int=Query(10,ge=10,le=100),
             sort:str=None,
             db:Session=Depends(get_db),current_user:User=Depends(admin_required)):
    return USerServices.all_user(db,page,limit,sort,search)


@router.get("/me",response_model=UserResponse)
def authme(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return USerServices.Authme(db,current_user)

@router.get("/user",response_model=UserResponse)
def single_user(user_id:int,db:Session=Depends(get_db),current_user:User=Depends(user_required)):
    return USerServices.single_user(db,user_id,current_user)

@router.put("/update",response_model=UserResponse)
def user_update(user_id:int,data:UserUpdate,db:Session=Depends(get_db),current_user:User=Depends(user_required)):
    return USerServices.update_user(db,data,user_id,current_user)


@router.delete("/delete")
def delete_user(user_id:int,db:Session=Depends(get_db),current_user:User=Depends(user_required)):
    return USerServices.delete_user(db,user_id,current_user)