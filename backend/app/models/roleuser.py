from app.core.database import Base
from sqlalchemy import Column,Integer,ForeignKey
from sqlalchemy.orm import relationship


class RoleUser(Base):
    
    __tablename__="roleusers"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    role_id=Column(Integer,nullable=True)
    
    
    user=relationship("User",back_populates="roleuser")