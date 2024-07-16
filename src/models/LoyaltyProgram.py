from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey
import uuid
from datetime import datetime, timedelta
from database.Database import Base
from sqlalchemy.orm import relationship

class LoyaltyProgram(Base):
    __tablename__ = "loyalty_programs"
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(100), ForeignKey("users.id"))
    points = Column(String(100))
    tier = Column(String(100))
    
   