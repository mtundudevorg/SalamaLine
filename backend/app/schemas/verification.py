from pydantic import BaseModel,EmailStr,Field


class EmailVerificationSend(BaseModel):
    email:EmailStr

class EmailVerificationConfirm(BaseModel):
    token:str=Field(min_length=32)

class PhoneVerificationSend(BaseModel):
    phone_number:str

class PhoneVerificationConfirm(BaseModel):
    code:str=Field(pattern=r"^\d{6}$")    