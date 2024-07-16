from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.Database import SessionLocal
from src.models.Booking import Booking
from src.schemas.Booking_Schemas import BookingResponse,BookingBase
import uuid

Booking_router = APIRouter()
db = SessionLocal()

#---------------------create_booking--------------------
@Booking_router.post("/create bookings", response_model=BookingBase)
def create_booking(booking: BookingBase):
    db_booking = Booking(
        id=str(uuid.uuid4()),
        user_id=booking.user_id,
        service_id = booking.service_id,
        start_date = booking.start_date,
        end_date = booking.end_date,
        status = booking.status,
        total_price = booking.total_price
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def cancel_booking(booking_id: str):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    booking.status = "cancelled"
    db.commit()
    db.refresh(booking)
    return booking