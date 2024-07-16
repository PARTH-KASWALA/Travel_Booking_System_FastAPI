import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Email configuration
sender_email = "parthkaswala2000@gmail.com"
receiver_email = "parthkaswala95@gmail.com"
password = "mydeoqcuaujnqpbz"
subject = "Your OTP Code"
otp = generate_otp()  # Generate OTP
message_text = f"Your OTP is {otp} which is valid for 1 minute" 

# Create the email message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the message text
message.attach(MIMEText(message_text, "plain"))

# Send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Mail sent successfully")
    server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")













# from fastapi import FastAPI,APIRouter,Depends,HTTPException
# from typing import List
# from database.database import SessionLocal
# import uuid
# from passlib.context import CryptContext
# from src.models.models_Lib import OTP,User
# import random
# from src.utils.otp_utils import generate_otp
# from src.schemas.schemas_Lib import OTPRequest,OTPVerify
# from datetime import datetime,timedelta
# import string
# import smtplib
# import random
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

# Otp=APIRouter()
# db= SessionLocal()



# def generate_otp(email: str):
#     otp_code = str(random.randint(100000, 999999))
#     expiration_time = datetime.now() + timedelta(minutes=5)
    
#     otp_entry = OTP(
#         email=email,
#         otp=otp_code,
#         expired_time=expiration_time,

#     )
#     db.add(otp_entry)
#     db.commit()
#     return otp_code

# def send_otp_email(email: str, otp_code: str):
#     sender_email = "parthkaswala2000@gmail.com"
#     password = ""
#     subject = "Your OTP Code"
#     message_text = f"Your OTP is {otp_code} which is valid for 5 minutes"

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = email
#     message["Subject"] = subject
#     message.attach(MIMEText(message_text, "plain"))

#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(sender_email, password)
#         server.sendmail(sender_email, email, message.as_string())
#         server.quit()
#         print("Mail sent successfully")
#     except Exception as e:
#         print(f"Failed to send email: {e}")

# @Otp.post("/generate_otp")
# def generate_otp_endpoint(request: OTPRequest):
#     email = request.email  
#     user = db.query(User).filter(User.email == email).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     otp_code = generate_otp(email)
#     send_otp_email(email, otp_code)
#     return {"message": "OTP generated and sent successfully to the provided email address."}




# @Otp.post("/verify_otp")
# def verify_otp(otp_verify: OTPVerify):
#     otp_entry = db.query(OTP).filter(
#         OTP.email == otp_verify.email,
#         OTP.otp == otp_verify.otp,
#         OTP.is_active == True,
#         OTP.expired_time > datetime.now(),
#         # OTP.is_deleted == False
#     ).first()

#     if otp_entry is None:
#         raise HTTPException(status_code=400, detail="Invalid or expired OTP")

#     otp_entry.is_active = False  
#     db.commit()

#     user = db.query(User).filter(User.email == otp_verify.email).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")

#     return {"message": "OTP verified successfully"}
