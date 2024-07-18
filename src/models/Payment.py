from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date, JSON,Text,Float
import uuid
from database.Database import Base
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship



class Payment(Base):
    __tablename__ = "payment"
    payment_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(50),ForeignKey("users.id"),nullable=False)
    booking_id = Column(String(50), ForeignKey("booking.booking_id"), nullable=False)
    amount = Column(String(50), nullable=False)
    payment_status = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    transaction_id =Column(String(50),default=lambda: str(uuid.uuid4()),nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


