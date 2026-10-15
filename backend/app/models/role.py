from app.core.database import Base
from sqlalchemy import Column,Integer,String



class Role(Base):
    __tablename__="roles"
    
    id=Column(Integer,primary_key=True)
    name=Column(String,unique=True)
    