from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey
import uuid
from datetime import datetime, timedelta
from database.Database import Base
from sqlalchemy.orm import relationship

# ----------------------------------------------Review Table------------------------------------------------------
class Review(Base):
    __tablename__ = "reviews"
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(100), ForeignKey("users.id"))
    service_id = Column(String(100), ForeignKey("services.id"))
    rating = Column(String(100))
    comment = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

   