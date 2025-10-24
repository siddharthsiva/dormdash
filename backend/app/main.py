from fastapi import FastAPI
from .db.database import Base, engine
from .routers import users, requests

app = FastAPI()

app.include_router(users.router)
app.include_router(requests.router)

Base.metadata.create_all(bind=engine)
