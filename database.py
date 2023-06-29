# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME=os.getenv('DB_NAME')
DB_USER=os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_HOSTNAME=os.getenv('DB_HOSTNAME')

DB_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}'

engine = create_engine(DB_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()