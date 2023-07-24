# app/routes/home.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from ..models import User
from ..utils.authentication import verify_password

router = APIRouter()

@router.post("/login/")
def login(username: str, password: str):
    # Here, you can implement your database logic to retrieve the user.
    # For this example, we'll just check the credentials and return a message.
    user = User(username=username, password=password)
    if verify_password(user.password, hashed_password_from_db):
        return {"message": "Login successful!"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
