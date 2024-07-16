from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
import uuid

#---------------------DestinationBase--------------------
class DestinationBase(BaseModel):
    name: str
    description: str
    country: str
    city: str
    attractions: str


#---------------------DestinationCreate--------------------
class DestinationCreate(DestinationBase):
    pass


#---------------------DestinationUpdate--------------------
class DestinationUpdate(DestinationBase):
    name: str
    description: str
    country: str
    city: str
    attractions: str


#---------------------DestinationResponse--------------------
class DestinationResponse(DestinationBase):
    id: str

