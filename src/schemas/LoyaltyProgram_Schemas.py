from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
import uuid



#---------------------LoyaltyProgramBase--------------------
class LoyaltyProgramBase(BaseModel):
    user_id: str
    points: str
    tier: str
    

#---------------------LoyaltyProgramCreate--------------------
class LoyaltyProgramCreate(LoyaltyProgramBase):
    pass


#---------------------LoyaltyProgramUpdate--------------------
class LoyaltyProgramUpdate(LoyaltyProgramBase):
    points: str
    tier: str


#---------------------LoyaltyProgramResponse--------------------
class LoyaltyProgramResponse(LoyaltyProgramBase):
    id: str


