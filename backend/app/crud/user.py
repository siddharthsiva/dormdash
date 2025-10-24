from sqlalchemy.orm import Session
from ..models.user import User

def get_leaderboard(db: Session, sort_by: str = "xp"):
    if sort_by == "karma":
        return db.query(User).order_by(User.karma.desc()).limit(10).all()
    return db.query(User).order_by(User.xp.desc()).limit(10).all()
