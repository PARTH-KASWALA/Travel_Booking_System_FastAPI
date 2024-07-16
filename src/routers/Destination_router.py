from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from src.models.Destination import Destination
from src.schemas.Destination_Schemas import DestinationBase,DestinationResponse,DestinationUpdate
from database.Database import SessionLocal
import uuid
from typing import List

Destination_router = APIRouter()
db = SessionLocal()

#---------------------Create Destination--------------------
@Destination_router.post("/create Destinations/", response_model=DestinationBase)
def create_destination(destination: DestinationBase):
    db_destination = Destination(
        name = destination.name,
        description = destination.description,
        country = destination.country,
        city = destination.city,
        attractions = destination.attractions
    )
    # db_destination = DestinationBase(**DestinationBase.dict())
    db.add(db_destination) #db: a database session that will be used to interact with the database
    db.commit() #This line commits the current transaction to the database, saving the changes made to the destination object.
    db.refresh(db_destination) #This line refreshes the destination object from the database, ensuring that it contains the latest data, including any changes made during the update process.
    return db_destination  #Finally, this line returns the updated destination object, which will be formatted according to the DestinationResponse model specified in the route decorator.



#---------------------get_all_destinations--------------------
@Destination_router.get("/get all the Destinatination", response_model=DestinationBase)
def get_all_destinations():
    destinations = db.query(Destination).all()
    return destinations


#---------------------get_destination_by_id--------------------
@Destination_router.get("/get_destination_by_id", response_model=DestinationResponse)
def get_destination_by_id(destination_id: str):
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    return destination


#---------------------Update_destination--------------------
@Destination_router.put("/Update destination", response_model=DestinationUpdate)
def Update_destination(destination_id: str, destination_update: DestinationUpdate):
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if not destination:
        raise Exception(status_code=404,  detail="Destination not found")
    db.commit()
    db.refresh(destination)
    return destination


#---------------------Delete_destination--------------------
@Destination_router.delete("/Delete destination")
def delete_destination(destination_id: str):
    destination = db.query(Destination).filter(Destination.id == destination_id).first() 
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    db.delete(destination)    
    db.commit()  
    return {"detail": "Destination deleted"} 





