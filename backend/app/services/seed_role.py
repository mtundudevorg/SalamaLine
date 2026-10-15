from app.models.role import Role
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status


roles=[
    {"name":"user"},
    {"name":"provider"},
    {"name":"admin"},
]


def seed_role(db:Session):

    for data in roles:
        existing=db.query(Role).filter(Role.name==data["name"]).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="role already seeded")
        
        roleuser=Role(
            name=data["name"]
        )
        db.add(roleuser)
    db.commit()
    
    return{
        "message":"role seeded successfuly"
    }        