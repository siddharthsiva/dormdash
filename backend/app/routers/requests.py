from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.request import Request
from pydantic import BaseModel

router = APIRouter()

class RequestCreate(BaseModel):
    title: str
    description: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/requests")
def create_request(request: RequestCreate, db: Session = Depends(get_db)):
    db_request = Request(**request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

@router.get("/requests")
def list_requests(db: Session = Depends(get_db)):
    return db.query(Request).all()
