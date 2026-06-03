from sqlalchemy.orm import Session

from backend.app.core.exceptions import raise_credentials_exception, raise_email_already_registered
from backend.app.core.security import create_access_token, hash_password, verify_password
from backend.app.repositories.user import create_user, get_user_by_email
from backend.app.schemas.user import TokenResponse, UserCreate, UserLogin


def register_user(
    db: Session,
    user_data: UserCreate,
):
    user_exist = get_user_by_email(db, user_data.email)
    if user_exist:
        raise_email_already_registered()
        
    password_hash = hash_password(user_data.password)
    user = create_user(
        db,
        email=user_data.email,
        password_hash=password_hash,
    )
    
    return user


def login_user(
    db: Session,
    user_data: UserLogin,
):
    user = get_user_by_email(db, user_data.email)
    if user is None:
        raise_credentials_exception()
    
    if verify_password(user_data.password, user.password_hash):
        token = TokenResponse(
            access_token=create_access_token(user.id),
            token_type="bearer",
        )
        return token
    
    raise_credentials_exception()