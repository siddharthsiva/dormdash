from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.database import SessionLocal
from ..crud.user import get_leaderboard

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/leaderboard")
def leaderboard(sort: str = "xp", db: Session = Depends(get_db)):
    return get_leaderboard(db, sort)
