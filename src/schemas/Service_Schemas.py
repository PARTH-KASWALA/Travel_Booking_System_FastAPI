from pydantic import BaseModel
from datetime import datetime

#---------------------ServiceBase--------------------
class ServiceBase(BaseModel):
    name: str
    description: str
    service_type: str
    price: float
    available: bool = True
    user_id:str

#---------------------ServiceCreate--------------------
class ServiceCreate(ServiceBase):
    name: str
    description: str
    service_type: str
    price: float
    available: bool = True
    user_id:str
    
#---------------------ServiceUpdate--------------------
class ServiceUpdate(ServiceBase):
    pass

#---------------------ServiceResponse--------------------
class ServiceResponse(ServiceBase):
    created_at: datetime
    updated_at: datetime
