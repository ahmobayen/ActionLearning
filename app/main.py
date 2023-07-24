# app/main.py

from fastapi import FastAPI
from .routes import auth, home

app = FastAPI()

# Register the routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(home.router, prefix="/home", tags=["Home"])
