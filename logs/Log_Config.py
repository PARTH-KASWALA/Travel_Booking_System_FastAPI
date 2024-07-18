
from pydantic import BaseModel,EmailStr,constr,Json,Field
from typing import List,Optional
from datetime import datetime,date


class PaymentBase(BaseModel) :
    booking_id : str
    user_id : str
    amount : str


#-----------------------log_congig----------------

from loguru import logger
logger.add(
    "logs/app.log",
    level="DEBUG",
    rotation="10 MB",
    format="{time:DD-MM-YYYY hh:mm:ss A} - {level} - {message}",
)



