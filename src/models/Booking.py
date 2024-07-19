from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database.Database import Base
import uuid
from datetime import datetime


# ----------------------------------------------Booking Table------------------------------------------------------
class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(100), ForeignKey("users.id"))
    service_id = Column(String(100), ForeignKey("services.id"))
    payment_id = Column(String(100), ForeignKey("payment.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String(100), default="confirmed")
    total_price = Column(Float)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
    
