from fastapi import APIRouter

import ango_auth.app.services.auth as auth_service
from ango_auth.app.core.config import Settings
from ango_auth.app.models.auth import SignInRequest, Token

settings = Settings()

auth_router = APIRouter()


@auth_router.post("/sign-in", response_model=Token)
def sign_in(sign_in_request: SignInRequest) -> Token:
    access_token = auth_service.sign_in(sign_in_request)
    return Token(access_token=access_token)
