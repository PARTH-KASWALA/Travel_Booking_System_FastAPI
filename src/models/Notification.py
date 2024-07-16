from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Boolean
from datetime import datetime
import uuid

from database.Database import Base



class Notification(Base):
    __tablename__ = 'NotificationInfo'
    
    id = Column(String(100),primary_key=True,default=str(uuid.uuid4()))
    message = Column(String(1000),nullable=False)
    recipient = Column(String(500), nullable=False) 
    status = Column(String(100), default="unread")
    u_id = Column(String, ForeignKey('UserInfo.id'), nullable=False)
    create_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    reminder_time = Column(DateTime, nullable=True) 
