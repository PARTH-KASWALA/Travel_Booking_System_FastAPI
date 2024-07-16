from pydantic import BaseModel
from typing import Optional



#---------------------NotificationAll--------------------
class NotificationAll(BaseModel):
    message : str
    recipient : str
    status : str
    user_id : str
    

#---------------------NotificationPatch--------------------
class NotificationPatch(BaseModel):
    message : Optional[str] = None
    recipient : Optional[str] = None
    status: Optional[str] = None
    user_id  : Optional[str] = None    
