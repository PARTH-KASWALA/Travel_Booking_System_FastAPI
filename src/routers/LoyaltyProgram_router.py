from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from src.models.LoyaltyProgram import LoyaltyProgram
from src.schemas.LoyaltyProgram_Schemas import LoyaltyProgramBase,LoyaltyProgramResponse,LoyaltyProgramUpdate
import uuid
from database.Database import SessionLocal
from typing import List


LoyaltyProgram_router = APIRouter(tags=["LoyaltyProgram"])
db = SessionLocal()

#---------------------create_all_loyalty_programs----------------------
@LoyaltyProgram_router.post("/crete LoyaltyProgram_router", response_model=LoyaltyProgramBase)
def create_all_loyalty_programs(loyaltyprogram:LoyaltyProgramBase):
    db_LoyaltyProgram = LoyaltyProgram(
        id=str(uuid.uuid4()),
        user_id = loyaltyprogram.user_id,
        points = loyaltyprogram.points,
        tier = loyaltyprogram.tier
    )
    db.add(db_LoyaltyProgram) #db: a database session that will be used to interact with the database
    db.commit() #This line commits the current transaction to the database, saving the changes made to the destination object.
    db.refresh(db_LoyaltyProgram) #This line refreshes the destination object from the database, ensuring that it contains the latest data, including any changes made during the update process.
    return db_LoyaltyProgram  


#---------------------get_all_loyalty_programs--------------------  
@LoyaltyProgram_router.get("/get_all_loyalty_programs", response_model=List[LoyaltyProgramResponse])
def get_all_loyalty_programs():
    programs = db.query(LoyaltyProgram).all()
    return programs


#---------------------get_loyalty_program_by_id--------------------
@LoyaltyProgram_router.get("/get_loyalty_program_by_id", response_model=LoyaltyProgramResponse)
def get_loyalty_program_by_id(program_id: int):
    program = db.query(LoyaltyProgram).filter(LoyaltyProgram.id == program_id)
    if not program:
        raise HTTPException(status_code=404, detail="Loyalty program not found")
    return program


#---------------------update_loyalty_program--------------------
@LoyaltyProgram_router.put("/update_loyalty_program", response_model=LoyaltyProgramResponse)
def update_loyalty_program(program_id: int, program_update: LoyaltyProgramUpdate):
    program = db.query(LoyaltyProgram).filter(LoyaltyProgram.id == program_id).first()
    if not program:
        raise HTTPException(status_code=404, detail="Loyalty program not found")
    db.commit()
    db.refresh(program)
    return program


