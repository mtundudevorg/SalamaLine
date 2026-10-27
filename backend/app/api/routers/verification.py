from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.verification import create_verification,confirm_verfication
from app.schemas.verification import EmailVerificationConfirm,PhoneVerificationConfirm


router=APIRouter(prefix="/verification",tags=["Account Verification"])


@router.post("/email/send")
def send_email_verification(
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)):
    

    return create_verification(
        db,
        current_user,
        channel="email"
        )



@router.post("/email/confirm")
def confirm_email_verfication(
    payload: EmailVerificationConfirm,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = confirm_verfication(
        db=db,
        current_user=current_user,
        channel="email",
        token=payload.token
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired token"
        )

    return {"message": "Email verified successfully"}

@router.post("/phone/send")
def send_phone_verification(db:Session=Depends(get_db),
                            current_user:User=Depends(get_current_user)):
    
    if current_user.is_phone_verified:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Phone already verified")
    
    verification,token=create_verification(
        db,
        user_id=current_user,
        channel="phone"
        )
    return {
        "message":"Phone verification request created"
    }
    
@router.post("/phone/confirm")
def confirm_phone_verfication(
    code:str,
    db:Session=Depends(get_db),
    current_user:User=Depends(get_current_user)):
    
    success=confirm_verfication(
        db=db,
        user_id=current_user,
        channel="phone",
        token=code,)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="invalid or expired verification code")
    return {
        "message":"Phone varified successfuly"
    }
    
