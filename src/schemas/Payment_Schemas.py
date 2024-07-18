from pydantic import BaseModel,EmailStr,constr,Json,Field
from typing import List,Optional
from datetime import datetime,date


class PaymentBase(BaseModel) :
    booking_id : str
    user_id : str
    amount : str



