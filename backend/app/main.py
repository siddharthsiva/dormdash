from fastapi import FastAPI
from .db.database import Base, engine
from .routers import users, requests

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(requests.router)
