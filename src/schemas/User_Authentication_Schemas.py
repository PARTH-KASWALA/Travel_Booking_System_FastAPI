from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime


#------------------UserBase------------------------
class UserBase(BaseModel):
    username: str
    email: str

#---------------------UserCreate--------------------
class UserCreate(BaseModel):
    username :str
    email :str
    mobile_no :str
    password :str

#---------------------Users--------------------
class Users(BaseModel):
    username :str
    email :str
    mobile_no :str
    password :str

#---------------------UserUpdate--------------------
class UserUpdate(BaseModel):
    username:str
    password:str
    
    
    
#---------------------UsersPatch--------------------
class UsersPatch(BaseModel):
    username :Optional[str]=None
    password :Optional[str]=None


#------------------OTP------------------------
class OTPRequest(BaseModel):
    email: EmailStr
class OTPVerify(BaseModel):
    email: EmailStr
    otp: str


