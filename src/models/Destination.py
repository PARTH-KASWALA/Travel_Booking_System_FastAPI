from sqlalchemy import Column, String, Boolean, DateTime
import uuid
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from database.Database import Base

# ----------------------------------------------Destination Table------------------------------------------------------
class Destination(Base):
    __tablename__ = "destinations"
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String(100), nullable=False)
    description = Column(String(100),nullable=False)
    country = Column(String(100),nullable=False)
    city = Column(String(100),nullable=False)
    attractions = Column(String(100),nullable=False)
    bookings_count = Column(String(100), default=0)