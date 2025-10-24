from sqlalchemy.orm import Session
from ..models.user import User

def apply_xp_and_karma(db: Session, user_id: int, urgency: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.xp += 10
        user.karma += 5 if urgency == "High" else 2
        db.commit()
