from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from backend.app.core.config import settings


def create_access_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=settings.access_token_expire_minutes)
    
    payload = {
        "sub": str(user_id),
        "exp": expire,
    }
    
    token = jwt.encode(
        payload, 
        settings.secret_key, 
        algorithm=settings.algorithm,
    )
    
    return token 


def decode_access_token(token: str) -> int:
    payload = jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.algorithm],
    )
    
    user_id = payload.get("sub")
    if user_id is None:
        raise JWTError("Token subject is missing")
    
    return int(user_id)