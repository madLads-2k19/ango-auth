from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from ango_auth.app.core.config import Settings
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

settings = Settings()


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def hash_password(password: bytes) -> bytes:
    return pwd_context.hash(password)


def verify_password(plain_password: bytes, hashed_password: bytes) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
