from sqlalchemy import Column,String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime
from database.Database import Base
import uuid

# ----------------------------------------------User Table------------------------------------------------------
class User(Base):
    __tablename__ = 'users'
    id = Column(String(100), primary_key=True, default=str(uuid.uuid4()))
    username = Column(String(100), unique=True,  nullable=False)
    email = Column(String(100), unique=True,  nullable=False)
    password = Column(String(100))
    mobile_no = Column(String(100))

    
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    

  
    
    
