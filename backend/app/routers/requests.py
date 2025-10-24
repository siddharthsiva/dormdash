from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from ..db.database import SessionLocal
from ..models.request import Request
from ..crud.request import mark_completed
from ..services.xp_engine import apply_xp_and_karma

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/requests")
def get_requests(dorm: Optional[str] = None, is_completed: Optional[bool] = None, db: Session = Depends(get_db)):
    query = db.query(Request)
    if dorm:
        query = query.filter(Request.location == dorm)
    if is_completed is not None:
        query = query.filter(Request.is_completed == is_completed)
    return query.all()

@router.patch("/requests/{id}/complete")
def complete_request(id: int, fulfiller_id: int, db: Session = Depends(get_db)):
    req = db.query(Request).filter(Request.id == id).first()
    mark_completed(db, id, fulfiller_id)
    apply_xp_and_karma(db, fulfiller_id, req.urgency)
    return {"message": "Request fulfilled"}
