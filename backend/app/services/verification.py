import hashlib,secrets,resend
from datetime import datetime,timezone,timedelta
from sqlalchemy.orm import Session
from app.models.verification import Verification
from app.models.user import User
from app.core.config import settings
from fastapi import HTTPException,status



def hash_token(token:str):
    return hashlib.sha256(token.encode("utf-8")).hexdigest()

def create_email_token():
    return secrets.token_urlsafe(32)

def create_phone_code():
    return f"{secrets.randbelow(1_000_000):06d}"

def create_verification(
    db:Session,
    current_user:User,
    channel:str
    
):
    if channel not in {"email","phone"}:
        raise ValueError("Unsuported verification channel")
    
    if channel=="email":
        if current_user.is_email_verified:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email alredy verified")
        if not current_user.email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="No email address found on your account")
        api_key=settings.RESEND_API_KEY
        email_from=settings.EMAIL_FROM
        if not api_key:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email services is not configured yet")
        token=create_email_token()
    else:
        if current_user.is_phone_verified:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Phone already verified")
            
        
    verification=Verification(
        user_id=current_user.id,
        channel=channel,
        token_hash=hash_token(token),
        expired_at=datetime.now(timezone.utc)+timedelta(minutes=10)
    )
    try:
        db.add(verification)
        db.flush()
        resend.api_key=api_key
        resend.Emails.send({
            "from":email_from,
            "to":[current_user.email],
            "subject":"Verify your salamaline email",
            "html":f"""
                <h2>Salamaline Email verification</h2>
                <p>Use the Token Below to Verify your email address:</p>
                <p><strong>{token}</strong></p>
                <p>this token expires in 10 minutes</p>
                <p>If you did not request this, please ignore this email.</p>
                """        
        })
       
        
        db.commit()
        db.refresh(verification)
    except HTTPException:
        db.rollback()
        raise
    except Exception as exc:
        db.rollback()
        print("RESENE EMAIL ERROR:",repr(exc))
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY,detail="Unable to send verification email,please try again")    
            
    
    return {
        "message":"verification request created"
    }    


def confirm_verfication(
    db: Session,
    current_user: User,
    channel: str,
    token: str
):
    verification = (
        db.query(Verification)
        .filter(
            Verification.user_id == current_user.id,
            Verification.channel == channel,
            Verification.used_at.is_(None)
        )
        .order_by(Verification.created_at.desc())
        .first()
    )

    if verification is None:
        return False

    now = datetime.now(timezone.utc)
    expired_at = verification.expired_at

    if expired_at.tzinfo is None:
        expired_at = expired_at.replace(tzinfo=timezone.utc)

    if expired_at <= now:
        return False

    if verification.attempts >= 5:
        return False

    verification.attempts += 1

    if not secrets.compare_digest(
        verification.token_hash,
        hash_token(token)
    ):
        db.commit()
        return False

    verification.used_at = now

    if channel == "email":
        current_user.is_email_verified = True
    elif channel == "phone":
        current_user.is_phone_verified = True

    db.commit()
    return True
