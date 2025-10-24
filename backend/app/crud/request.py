from sqlalchemy.orm import Session
from ..models.request import Request

def mark_completed(db: Session, request_id: int, fulfiller_id: int):
    req = db.query(Request).filter(Request.id == request_id).first()
    if req:
        req.is_completed = True
        req.fulfiller_id = fulfiller_id
        db.commit()
