from pydantic import BaseModel
from typing import Optional

class RequestCreate(BaseModel):
    item: str
    location: str
    urgency: str
    reward: int
    requester_id: int

class RequestOut(BaseModel):
    id: int
    item: str
    location: str
    urgency: str
    reward: int
    is_completed: bool
    requester_id: int
    fulfiller_id: Optional[int]

    class Config:
        orm_mode = True
