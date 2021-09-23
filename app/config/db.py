import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base as decBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import false, true
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"] 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=false, autoflush=false, bind=engine)

Base = decBase()