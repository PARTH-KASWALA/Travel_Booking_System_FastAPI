from fastapi import FastAPI,APIRouter
from src.routers.User_Authentication_router import users,Otp
from src.routers.Booking_router import Booking_router
from src.routers.Destination_router import Destination_router
from src.routers.LoyaltyProgram_router import LoyaltyProgram_router
from src.routers.Promotion_router import Promotion_router
from src.routers.Review_router import Review_router
from src.routers.Service_router import Service_router
from src.routers.UserPreferences_router import UserPreferences_router
from src.routers.Notification_router import Notifications
# from src.routers.Notification_router 


app = FastAPI()
app.include_router(users)
app.include_router(Otp)
app.include_router(Booking_router)
app.include_router(Destination_router)
app.include_router(LoyaltyProgram_router)
app.include_router(Promotion_router)
app.include_router(Review_router)
app.include_router(Service_router)
app.include_router(UserPreferences_router)
app.include_router(Notifications)