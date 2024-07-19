from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime


#---------------------BookingBase--------------------
class BookingBase(BaseModel):
    user_id: str
    service_id: str
    payment_id : str
    start_date: datetime
    end_date: datetime
    status: str = "confirmed"
    total_price: float

#---------------------BookingResponse--------------------
class BookingResponse(BookingBase):
    id: str
    created_at: datetime
    updated_at: datetime