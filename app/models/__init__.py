from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.sql import func
from app.config.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())



class poll(Base):
    __tablename__= 'poll'

    id = Column(Integer, primary_key=True, autoincrement=True)
    polltype = Column(String, nullable=False)