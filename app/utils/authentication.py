# app/utils/authentication.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    hashed_password = pwd_context.hash(password)
    return hashed_password[:15]  # Limit the length to 15 characters
