from sqlalchemy import Column, String, Boolean, DateTime
import uuid
from datetime import datetime, timedelta
from database.Database import Base


# ----------------------------------------------OTP Table------------------------------------------------------
class OTP(Base):
    __tablename__ = "otp"
    
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    email = Column(String(100), nullable=False)
    otp = Column(String(100), nullable=False)
    expired_time = Column(DateTime, default=lambda: datetime.now() + timedelta(minutes=1))
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


