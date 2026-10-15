from app.core.database import Base
from sqlalchemy import Column,String,Integer,DateTime,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True)
    full_name=Column(String,nullable=False)
    email=Column(String,nullable=True,unique=True)
    Phone=Column(String,nullable=True,unique=True)
    password=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    
    roleuser=relationship("RoleUser",back_populates="user",cascade="all, delete-orphan")