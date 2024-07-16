from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
import uuid


#---------------------UserPreferencesBase--------------------
class UserPreferencesBase(BaseModel):
    user_id: str
    preferred_language: str
    preferred_currency: str
    

#---------------------UserPreferencesCreate--------------------
class UserPreferencesCreate(UserPreferencesBase):
    pass


#---------------------UserPreferencesUpdate--------------------
class UserPreferencesUpdate(UserPreferencesBase):
    preferred_language: str
    preferred_currency: str


#---------------------UserPreferencesResponse--------------------
class UserPreferencesResponse(UserPreferencesBase):
    user_id: str

