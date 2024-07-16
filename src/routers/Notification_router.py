import os
from fastapi import FastAPI, HTTPException, APIRouter
from database.Database import SessionLocal
from passlib.context import CryptContext
from src.schemas.Notification_Schemas import NotificationAll
from src.models.User_Authentication import User
from src.models.Notification import Notification
from datetime import datetime, timedelta
from dotenv import load_dotenv
from src.utils.Email import send_notification_via_email


load_dotenv()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
Notifications = APIRouter(tags=["Notification"])
db = SessionLocal()

#---------------------create_notification--------------------
@Notifications.post("/notifications/", response_model=NotificationAll)
def create_notification(notification: NotificationAll):
    user = db.query(User).filter(User.id == notification.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Notification not found")

    if notification.recipient != user.email:
        raise HTTPException(status_code=400, detail="Recipient email does not match user's email")

    reminder_time = datetime.now() + timedelta(minutes=1)

    notification_record = Notification(
        message=notification.message,
        recipient=notification.recipient,
        status='unread',
        u_id=notification.user_id,
        reminder_time=reminder_time
    )

    db.add(notification_record)
    db.commit()

    print(f"Notification for {user.email}: {notification.message}")
    
    if send_notification_via_email(user.email, notification.message):
        notification_record.status = 'read'
        db.commit()
        return notification_record
    else:
        raise HTTPException(status_code=500, detail="Failed to send SMS notification")
