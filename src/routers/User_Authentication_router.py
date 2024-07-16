from fastapi import APIRouter,HTTPException,Header
from typing import List
from database.Database import SessionLocal
import uuid
from passlib.context import CryptContext
from src.models.OTP import OTP
from src.models.User_Authentication import User
from src.schemas.User_Authentication_Schemas import Users,UsersPatch,UserCreate,UserBase
from src.utils.Token import get_encode_token,decode_token_user_id,login_token
from src.schemas.User_Authentication_Schemas import OTPRequest,OTPVerify
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime,timedelta
from src.utils.Otp_Utils import generate_otp


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users=APIRouter()
db= SessionLocal()


 # ----------------------------------------------encode_token_id------------------------------------------------------
@users.get("/encode_token_id")
def encode_token_id(id:str):
    access_token=get_encode_token(id)
    return access_token



 # ----------------------------------------------Create_User_post------------------------------------------------------
@users.post("/Create_User_post", response_model=Users)
def create_register_user(user: Users):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(
            status_code=401,
            detail="Same email found. Please try another one!"
        )
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(
            status_code=401,
            detail="Same username found. Please try another one!"
        )
    if db.query(User).filter(User.mobile_no == user.mobile_no).first():
        raise HTTPException(
            status_code=401,
            detail="Same mobile number found. Please try another one!"
        )

    new_user = User(
        id=str(uuid.uuid4()),
        username=user.username,
        email=user.email,
        mobile_no=user.mobile_no,
        password=pwd_context.hash(user.password),
        
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



# ----------------------------------------------get_all_users-----------------------------------------------------
@users.get("/get_all_users",response_model=List[Users])
def get_all_user():
    db_user=db.query(User).filter(User.is_active == True,User.is_verified == True).all()
    if db_user is None :
        raise HTTPException (status_code=404,detail="User Not Found")
    return db_user



 # ----------------------------------------------get_employee_by_id------------------------------------------------------
@users.get("/get_user_by_token_id/", response_model=Users)
def get_employee_by_id(token = Header(...)):
    user_id=decode_token_user_id(token)
    db_user = db.query(User).filter(User.id == user_id, User.is_active == True,User.is_verified == True).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found !!!")
    return db_user



# ----------------------------------------------update_user_by_token------------------------------------------------------
@users.put("/update_user_by_token/")
def update_user_data(user: Users, token: str = Header(...)):
    user_id = decode_token_user_id(token)
    db_user = db.query(User).filter(User.id == user_id, User.is_active == True, User.is_verified == True).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="User Not Found!!!!")

    if db.query(User).filter(User.email == user.email, User.id != user_id).first():
        raise HTTPException(status_code=401, detail="Same email found. Please try another one!")
    
    if db.query(User).filter(User.username == user.username, User.id != user_id).first():
        raise HTTPException(status_code=401, detail="Same username found. Please try another one!")
    
    if db.query(User).filter(User.mobile_no == user.mobile_no, User.id != user_id).first():
        raise HTTPException(status_code=401, detail="Same mobile number found. Please try another one!")

    db_user.id = str(uuid.uuid4()),
    db_user.username = user.username,
    db_user.email = user.email,
    db_user.mobile_no = user.mobile_no,
    db_user.password = pwd_context.hash(user.password)

    db.commit()
    db.refresh(db_user)
    
    return {"message": "Your details have been successfully updated!"}



# ----------------------------------------------update[PATCH]_user_by_token------------------------------------------------------
@users.patch("/update_user_patch")
def update_employee_patch(employeee: UsersPatch,token = Header(...)):
    user_id = decode_token_user_id(token)
    find_user = db.query(User).filter(User.id == user_id, User.is_active == True,User.is_verified == True).first()
    if find_user is None:   
        raise HTTPException(status_code=404, detail="User Not Found")
    update_data = employeee.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(find_user, key, value)
    db.commit()
    db.refresh(find_user) 
    return {"message": "Details changed successfully", "User": find_user}



# ----------------------------------------------Delete_User_by_token------------------------------------------------------
@users.delete("/delete_user_by_token/")
def delete_employee(token = Header(...)):
    emp_id=decode_token_user_id(token)
    db_user=db.query(User).filter(User.id == emp_id ,User.is_active == True,User.is_verified == True).first()
    if db_user is None :
        raise HTTPException (status_code=404,detail="User Not Found.....")
    db_user.is_active=False
    db_user.is_deleted=True
    db.commit()
    return f"User Deleted Successfully !!!!!!!!!!!!!"



# ----------------------------------------------forgotpass_user_by_token------------------------------------------------------    
@users.put("/forgotpass_user_by_token/")
def forgotpass_user_by_token(new_pass:str,token =Header(...)):
    user_id=decode_token_user_id(token)
    db_user=db.query(User).filter(User.id==user_id , User.is_active == True,User.is_verified == True).first()
    if db_user is None:
        raise HTTPException(status_code=404,detail="User NOt Found!!!")
    db_user.password=pwd_context.hash(new_pass)
    db.commit() 
    return f"Password Change Successfully"



# ----------------------------------------------reset_pass_user_token------------------------------------------------------    
@users.put("/reset_pass_user_token/")
def reset_pass_user(old_pass: str, new_pass: str, token = Header(...)):
    user_id = decode_token_user_id(token)
    db_user = db.query(User).filter(User.id == user_id, User.is_active == True,User.is_verified == True).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if pwd_context.verify(old_pass, db_user.password):
        db_user.password = pwd_context.hash(new_pass)
        db.commit()
        return {"message": "Password Reset Successfully!!!"}
    else:
        raise HTTPException(status_code=400, detail="Old password does not match")



# ---------------------------------------------encode_token_login----------------------------------------------------- 
@users.get("/encode_token_login")
def encode_token_id(id:str,password:str,email:str):
    access_token=login_token(id,password,email)
    return access_token


# ----------------------------------------------LOGIN_USER-----------------------------------------------------    
@users.get("/logging_users")
def logging_user(email:str, password:str):
    # breakpoint()
    db_user = db.query(User).filter(User.email == email,User.is_active == True,User.is_deleted == False,User.is_verified == True).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not pwd_context.verify(password, db_user.password):
        raise HTTPException(status_code=404, detail="Password is incorrect")
    access_token = login_token(db_user.id, email, password)
    return  access_token





# ----------------------------------------------OTP------------------------------------------------------
Otp=APIRouter()
db= SessionLocal()

def generate_otp(email: str):
    otp_code = str(random.randint(100000, 999999))
    expiration_time = datetime.now() + timedelta(minutes=5)
    
    otp_entry = OTP(
        email=email,
        otp=otp_code,
        expired_time=expiration_time,
    )
    db.add(otp_entry)
    db.commit()
    return otp_code

def send_otp_email(email: str, otp_code: str):
    sender_email = "parthkaswala2000@gmail.com"
    password = "zdbyepwrhuvenbmp"
    subject = "Your OTP Code"
    message_text = f"Your OTP is {otp_code} which is valid for 5 minutes"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(message_text, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
        print("Mail sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# --------------------------------------------------GENERATE_OTP ------------------------------------------------------------
@Otp.post("/generate_otp")
def generate_otp_endpoint(request: OTPRequest):
    email = request.email  
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    otp_code = generate_otp(email)
    send_otp_email(email, otp_code)
    return {"message": "OTP generated and sent successfully to the provided email address."}



# --------------------------------------------------VERIFICATION_OTP ------------------------------------------------------------
@Otp.post("/verify_otp")
def verify_otp(otp_verify: OTPVerify):
    otp_entry = db.query(OTP).filter(
        OTP.email == otp_verify.email,
        OTP.otp == otp_verify.otp,
        OTP.is_active == True,
        OTP.expired_time > datetime.now(),
        # OTP.is_deleted == False
    ).first()
    if otp_entry is None:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")
    otp_entry.is_active = False  
    user = db.query(User).filter(User.email == otp_verify.email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_verified = True
    db.delete(otp_entry)
    db.commit()

    return {"message": "OTP verified successfully"}






















