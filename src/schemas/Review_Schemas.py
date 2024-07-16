from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
import uuid

#---------------------ReviewBase--------------------
class ReviewBase(BaseModel):
    user_id: str
    service_id: str
    rating: str
    comment: str


#---------------------ReviewCreate--------------------
class ReviewCreate(ReviewBase):
    pass


#---------------------ReviewResponse--------------------
class ReviewResponse(ReviewBase):
    id: str
    created_at: datetime
    updated_at: datetime
