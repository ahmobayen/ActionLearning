# app/routes/auth.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models import User
from ..utils.authentication import get_password_hash
from ..database import get_db

router = APIRouter()

@router.post("/register/", response_model=User)
def register(username: str, password: str, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(password)
    user = User(username=username, password=hashed_password)

    # Save the user to the database
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
