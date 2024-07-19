from datetime import datetime,timedelta
from fastapi import HTTPException,status
from dotenv import load_dotenv
import os
from jose import jwt,JWTError
load_dotenv()
SECRET_KEY = str(os.environ.get("SECRET_KEY"))
ALGORITHM = str(os.environ.get("ALGORITHM"))

#---------------------get_encode_token--------------------
def get_encode_token(id):
    payload = {
        "user_id" : id,
        "exp" : datetime.now() + timedelta(hours=1)
    }
    access_token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    print(type(access_token))
    return access_token

def decode_token_user_id(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        emp_id = payload.get("id")
        if not emp_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return emp_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )



def decode_token_user_name(token):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user_name = payload.get("user_name")
        if not user_name:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token",
            )
        return user_name
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )


def decode_token_password(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        password = payload.get("password")
        if not password:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token"
            )
        return password
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )

def decode_token_email(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        if not email:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token"
            )
        return email
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )




def login_token(id,user_name,password):
    payload = {
        "id" :id,
        "user_name" : user_name,
        "password" : password,
        "exp" : datetime.now() + timedelta(hours=1)
    }
    access_token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
    print(type(access_token))
    return access_token
















# from src.models.models_Lib import User
# from database.database import SessionLocal

# db = SessionLocal()


# def verify_user(user_id):
#     find_user_with_is_verified_true = (
#         db.query(User).filter(User.id == user_id, User.is_verified == True).first()
#     )
#     if not find_user_with_is_verified_true:
#         return False
#     else:
#         return True 
    


# def decode_token_user_id_id(token: str) -> str:
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: str = payload.get("sub")
#         if user_id is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return user_id
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")








