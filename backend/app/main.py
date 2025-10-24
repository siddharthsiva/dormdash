from fastapi import FastAPI
from app.db.database import Base, engine
from app.routers import users, requests

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)
app.include_router(requests.router)
