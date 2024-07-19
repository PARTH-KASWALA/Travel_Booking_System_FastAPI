from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey
import uuid
from datetime import datetime, timedelta
from database.Database import Base
from sqlalchemy.orm import relationship


# ----------------------------------------------UserPreferences Table------------------------------------------------------
class UserPreferences(Base):
    __tablename__ = "user_preferences"
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(100), ForeignKey("users.id"))
    preferred_language = Column(String(100), nullable=False)
    preferred_currency = Column(String(100),  nullable=False)



