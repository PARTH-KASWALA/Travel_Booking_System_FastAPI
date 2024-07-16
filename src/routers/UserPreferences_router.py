from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from src.models.UserPreferences import UserPreferences
from src.schemas.UserPreferences_Schemas import UserPreferencesBase,UserPreferencesResponse,UserPreferencesUpdate
import uuid
from database.Database import SessionLocal
from typing import List

UserPreferences_router = APIRouter()
db = SessionLocal()


#---------------------create_user_preferences--------------------
@UserPreferences_router.post("/create_user_preferences", response_model=UserPreferencesBase)
def create_user_preferences(userpreference : UserPreferencesBase):
    db_user_preferences = UserPreferences(
        id=str(uuid.uuid4()),
        user_id = userpreference.user_id,
        preferred_language = userpreference.preferred_language,
        preferred_currency = userpreference.preferred_currency,
    )
    db.add(db_user_preferences) #db: a database session that will be used to interact with the database
    db.commit() #This line commits the current transaction to the database, saving the changes made to the destination object.
    db.refresh(db_user_preferences) #This line refreshes the destination object from the database, ensuring that it contains the latest data, including any changes made during the update process.
    return db_user_preferences  


#---------------------get_user_preferences--------------------
@UserPreferences_router.get("/get_user_preferences", response_model=UserPreferencesResponse)
def get_user_preferences(user_id: str):
    preferences = db.query(UserPreferences).filter(UserPreferences.user_id == user_id).first()
    if not preferences:
        raise HTTPException(status_code=404, detail="Preferences not found")
    return preferences


#---------------------update_user_preferences--------------------
@UserPreferences_router.delete("/update_user_preferences", response_model=UserPreferencesResponse)
def update_user_preferences(user_id : str,preferences_update: UserPreferencesUpdate):
    preferences = db.query(UserPreferences).filter(UserPreferences.user_id == user_id).first()
    if not preferences:
        raise HTTPException(status_code=404, detail="Preferences not found")
    db.commit()
    db.refresh(preferences)
    return preferences