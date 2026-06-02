from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.app.models import User


def get_user_by_email(
    db: Session,
    email: str,
):
    user = db.scalars(
        select(User).where(User.email == email)
    ).first()
 
    return user


def create_user(
    db: Session,
    email: str,
    password_hash: str,
):
    user = User(
        email=email,
        password_hash=password_hash,
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

