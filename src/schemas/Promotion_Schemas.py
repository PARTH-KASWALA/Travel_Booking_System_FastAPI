from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
import uuid




#---------------------PromotionBase--------------------
class PromotionBase(BaseModel):
    title: str
    description: str
    discount_percentage: float
    start_date: datetime
    end_date: datetime
    active: bool = True


#---------------------PromotionCreate--------------------
class PromotionCreate(PromotionBase):
    pass


#---------------------PromotionUpdate--------------------
class PromotionUpdate(PromotionBase):
    title: str
    description: str
    discount_percentage: float
    start_date: datetime
    end_date: datetime
    active: bool = True


#---------------------PromotionResponse--------------------
class PromotionResponse(PromotionBase):
    id: str
