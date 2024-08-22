from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from src.models.Service import Service
from src.schemas.Service_Schemas import ServiceBase,ServiceResponse,ServiceCreate
import uuid
from database.Database import SessionLocal
from typing import List

Service_router = APIRouter(tags=["Service"])
db = SessionLocal()

#---------------------create_service--------------------
@Service_router.post("/create_service", response_model=ServiceResponse)
def create_service(service: ServiceCreate):
    db_service = Service(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service


#---------------------get_services--------------------
@Service_router.get("/get_services", response_model=List[ServiceResponse])
def get_services(skip: int = 0, limit: int = 10):
    services = db.query(Service).offset(skip).limit(limit).all()
    return services

#---------------------get_service--------------------
@Service_router.get("/Service_router", response_model=ServiceResponse)
def get_service(service_id: str):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service


#---------------------update_service--------------------
@Service_router.put("/update_service", response_model=ServiceResponse)
def update_service(service_id: int, service: ServiceCreate):
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Service not found")
    db.commit()
    db.refresh(db_service)
    return db_service


#---------------------delete_service--------------------
@Service_router.delete("/delete_service", status_code=404)
def delete_service(service_id: str):
    db_service = db.query(Service).filter(Service.id == service_id).first()
    if not db_service:
        raise HTTPException(status_code=404, detail="Service not found")
    db.delete(db_service)
    db.commit()
    return
