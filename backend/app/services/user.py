from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.repositories.user import create_user, get_user_by_email
from backend.app.schemas.user import UserCreate


def hash_password(password: str) -> str:
    return "hashed_" + password


def register_user(
    db: Session,
    user_data: UserCreate,
):
    user_exist = get_user_by_email(db, user_data.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    password_hash = hash_password(user_data.password)
    user = create_user(
        db,
        email=user_data.email,
        password_hash=password_hash,
    )
    
    return user

