from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from datetime import datetime
from ..db.database import Base

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    location = Column(String)
    urgency = Column(String)
    reward = Column(Integer)
    requester_id = Column(Integer, ForeignKey("users.id"))
    fulfiller_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
