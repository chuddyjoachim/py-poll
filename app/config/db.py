import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base as decBase
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql.expression import false, true
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv()

SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"] 

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(Sessionlocal)

Base = decBase()
Base.query = db_session.query_property()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    except:
        db.close()
