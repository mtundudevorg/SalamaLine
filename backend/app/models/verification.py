from app.core.database import Base
from sqlalchemy import Column,String,Integer,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Verification(Base):
    __tablename__="verifications"
    
    
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    channel=Column(String,nullable=False)
    token_hash=Column(String,nullable=False)
    attempts=Column(Integer,nullable=False,default=0)
    expired_at=Column(DateTime(timezone=True),nullable=False)
    used_at=Column(DateTime(timezone=True),nullable=True)
    created_at=Column(DateTime(timezone=True),default=datetime.now)
    
    
    
    user=relationship("User",back_populates="verify")