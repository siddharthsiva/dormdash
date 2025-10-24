from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    dorm: str

class UserOut(BaseModel):
    id: int
    name: str
    dorm: str
    xp: int
    karma: int

    class Config:
        orm_mode = True
