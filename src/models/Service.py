from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey,Float
import uuid
from datetime import datetime, timedelta
from database.Database import Base
from sqlalchemy.orm import relationship


class Service(Base):
    __tablename__ = "services"
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(100), ForeignKey('users.id'))
    name = Column(String(100), index=True)
    description = Column(String(100))
    service_type = Column(String(100))
    price = Column(Float)
    available = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
