from app.models.user import User
from sqlalchemy.orm import Session
from app.schemas.user import UserCeate,UserUpdate
from fastapi import HTTPException,status
from sqlalchemy import or_,asc,desc
import math
from app.models.role import Role
from app.models.roleuser import RoleUser
from app.core.security import hashing



class USerServices:
    
    
    @staticmethod
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
        
     
    @staticmethod
    def all_user(db:Session,page,limit,sort,search):
        user=db.query(User)
        
        if search:
            user=user.filter(or_(
                User.full_name.ilike(f"%{search}%"),
                User.Phone.ilike(f"%{search}%")
            ))
        
        if sort:
            if sort=="full_name":
                user=user.order_by(asc(User.full_name))
            else:
                user=user.order_by(desc(User.full_name))
        else:
            if sort=="created_at":
                user=user.order_by(asc(User.created_at))
            else:
                user=user.order_by(desc(User.created_at))
        
        
        skip=(page-1)*limit
        total=user.count()
        total_pages=math.ceil(total/limit)
        
        user=user.offset(skip).limit(limit).all()     
        
        
        return{
            "Pagination":{
              "page":page,
              "limit":limit,
              "total_user":total,
              "total_pages":total_pages,
              "has_next":page<total,
              "has_previous":page>1
            },
            "user":user
        }  
              
    @staticmethod
    def single_user(db:Session,user_id):
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")                    
        
        return user
    
    @staticmethod
    def update_user(db:Session,data:UserUpdate,user_id):
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")
                           
        # user=db.query(User).filter(User.email==data.email,User.Phone==data.Phone).first()
        # if user:
        #     raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="email or password all used")
        # if not data.email and data.phone:
        #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="one or both email or phone number is required")
        
        user.full_name=data.full_name
        user.email=data.email
        user.Phone=data.Phone
        
        db.commit()
        db.refresh(user)
        
        return user
        
    
    
    @staticmethod
    def delete_user(db:Session,user_id):
        user=db.query(User).filter(User.id==user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with iid  {user_id} not found")
        db.delete(user)
        db.commit()
        
        return{
            "message":"user successfuly deleted"
        }
        
                    
        
        
            