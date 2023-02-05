from uuid import UUID

from pydantic import BaseModel, EmailStr


class SignInRequest(BaseModel):
    email: EmailStr
    password: bytes


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    user_id: UUID
    email: EmailStr
