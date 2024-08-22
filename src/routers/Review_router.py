from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from src.models.Review import Review
from src.schemas.Review_Schemas import ReviewBase,ReviewResponse 
import uuid
from database.Database import SessionLocal
from typing import List


Review_router = APIRouter(tags=["Review"])
db = SessionLocal()

#---------------------create_all_review--------------------
@Review_router.post("/crete_all_reviews", response_model=ReviewBase)
def create_all_review(review : ReviewBase):
    db_review = Review(
        id=str(uuid.uuid4()),
        user_id = review.user_id,
        service_id = review.service_id,
        rating = review.rating,
        comment = review.comment,
    )
    db.add(db_review) #db: a database session that will be used to interact with the database
    db.commit() #This line commits the current transaction to the database, saving the changes made to the destination object.
    db.refresh(db_review) #This line refreshes the destination object from the database, ensuring that it contains the latest data, including any changes made during the update process.
    return db_review  


#---------------------get_all_reviews--------------------
@Review_router.get("/get all reviews", response_model=List[ReviewResponse])
def get_all_reviews():
    reviews = db.query(Review).all()
    return reviews


#---------------------get_reviews_for_service--------------------
@Review_router.get("/get_reviews_for_service",response_model=List[ReviewResponse])
def get_reviews_for_service(service_id : str):
    reviews = db.query(Review).filter(Review.service_id == service_id).all()
    return reviews


#---------------------get_reviews_by_user--------------------
@Review_router.get("get_reviews_by_user", response_model=List[ReviewResponse])
def get_reviews_by_user(user_id: int):
    reviews = db.query(Review).filter(Review.user_id == user_id).all()
    return reviews

