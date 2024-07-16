from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

url = str(os.environ.get("DB_URL"))
engine = create_engine(url, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
