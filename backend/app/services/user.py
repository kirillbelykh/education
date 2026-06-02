from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.security import create_access_token
from backend.app.repositories.user import create_user, get_user_by_email
from backend.app.schemas.user import TokenResponse, UserCreate, UserLogin


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


def verify_password(password: str, password_hash: str) -> bool:
    return password_hash == hash_password(password)


def login_user(
    db: Session,
    user_data: UserLogin,
):
    user = get_user_by_email(db, user_data.email)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    
    if verify_password(user_data.password, user.password_hash):
        token = TokenResponse(
            access_token=create_access_token(user.id),
            token_type="bearer",
        )
        return token
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password",
    )