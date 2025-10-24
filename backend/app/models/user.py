from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    xp = Column(Integer, default=0)
    karma = Column(Integer, default=0)
    dorm = Column(String, nullable=True)
