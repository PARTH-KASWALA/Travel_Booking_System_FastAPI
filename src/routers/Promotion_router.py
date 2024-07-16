from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from src.models.Promotion import Promotion
from src.schemas.Promotion_Schemas import PromotionBase,PromotionResponse,PromotionUpdate
import uuid
from database.Database import SessionLocal
from typing import List


Promotion_router = APIRouter()
db = SessionLocal()

#---------------------create_Promotion--------------------
@Promotion_router.post("/Create Promotion", response_model=PromotionBase)
def create_Promotion(promotion: PromotionBase):
    db_promotion = Promotion(**promotion.dict()) #part unpacks the dictionary representation of the promotion object and uses it to initialize the new Promotion object.
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion


#---------------------Promotion_router--------------------
@Promotion_router.get("/get_all_promotions", response_model=List[PromotionResponse])
def get_all_promotions():
    promotions = db.query(Promotion).all()
    return promotions


#---------------------get_promotion_by_id--------------------
@Promotion_router.get("/get_promotion_by_id", response_model=PromotionResponse)
def get_promotion_by_id(promotion_id: str):
    promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion



#---------------------update_promotion--------------------
@Promotion_router.put("/update_promotion", response_model=PromotionResponse)
def update_promotion(promotion_id: str, promotion_update: PromotionUpdate):
    promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    db.commit()
    db.refresh(promotion)
    return promotion


#---------------------delete_Promotion--------------------
@Promotion_router.delete("/Delete Promotion")
def delete_Promotion(promotion_id: str):
    promotion = db.query(Promotion).filter(Promotion.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    db.delete(promotion)
    db.commit()
    return {"detail": "Promotion deleted"}