

from fastapi import FastAPI, HTTPException, APIRouter, Depends, Security
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import logging
from database.Database import SessionLocal
# from src.schemas.tour_sch import TourBase 
from logs.Log_Config import logger
# from src.models.tours_mod import Tour
import uuid
from src.schemas.Booking_Schemas import BookingBase
from src.models.Booking import Booking
from src.models.User_Authentication import User
from src.models.Payment import Payment
from src.schemas.Payment_Schemas import PaymentBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

pwdd = APIRouter()
db = SessionLocal()


@pwdd.post("/make_payments", response_model=PaymentBase)
def make_payments(pay: PaymentBase):
    breakpoint()
    try:
        db_payment = Payment(
            payment_id=str(uuid.uuid4()),
            user_id=pay.user_id,
            booking_id=pay.booking_id,
            amount=pay.amount,
            payment_status="Completed"
        )
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        
        # Send payment confirmation email
        send_payment_confirmation_email(pay.user_id, pay.amount)
        
        return db_payment
    except Exception as e:
        # logger.error(f"Error making payment: {e}")
        raise HTTPException(status_code=500, detail="Failed to process payment")

def send_payment_confirmation_email(user_id: str, amount: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        sender_email = "ujasmungla@gmail.com"  # Replace with your sender email
        password = "wfrdhevqfopcssre"  # Replace with your sender email password
        subject = "Payment Confirmation"
        
        # Convert amount to float
        amount_float = float(amount)

        message_text = f"Dear {user.username},\n\nYour payment of ₹ {amount_float:.2f} has been successfully processed.\n\nThank you for using our service."

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = user.email
        message["Subject"] = subject
        message.attach(MIMEText(message_text, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, user.email, message.as_string())
            server.quit()
            logger.info(f"Payment confirmation email sent successfully to: {user.email}")
        except Exception as e:
            logger.error(f"Failed to send payment confirmation email: {e}")
            raise HTTPException(status_code=500, detail="Failed to send payment confirmation email")
    else:
        logger.warning(f"User not found with user_id: {user_id}")
        raise HTTPException(status_code=404, detail="User not found")

