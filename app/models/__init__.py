import uuid

from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.sql import func
from app.config.db import Base

def get_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=get_uuid())
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())


class Poll(Base):
    __tablename__ = "poll"

    id = Column(String, primary_key=True, default=get_uuid())
    polltype = Column(String, nullable=False)
