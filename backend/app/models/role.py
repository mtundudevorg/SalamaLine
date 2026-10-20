from app.core.database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship



class Role(Base):
    __tablename__="roles"
    
    id=Column(Integer,primary_key=True)
    name=Column(String,unique=True)
    
    role_users=relationship("RoleUser",back_populates="role")
    