from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey,Float
import uuid
from datetime import datetime, timedelta
from database.Database import Base


class Promotion(Base):
    __tablename__ = "promotions"
    id = Column(String(100),  primary_key=True, default=str(uuid.uuid4()))
    title = Column(String(100))
    description = Column(String(100))
    discount_percentage = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    active = Column(Boolean, default=True)

