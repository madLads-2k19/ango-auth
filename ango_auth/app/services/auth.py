import json

from ango_auth.app.core.exceptions import AuthException
from ango_auth.app.core.crypto.auth import verify_password, create_access_token
from ango_auth.app.models.auth import SignInRequest, TokenData
import ango_auth.app.services.web as web_service
from ango_auth.app.models.user import UserDb


def sign_in(sign_in_request: SignInRequest) -> str:
    user: UserDb = web_service.get_user_details(sign_in_request.email)

    if not user or not verify_password(sign_in_request.password, user.pass_hash):
        raise AuthException(message="Incorrect email or password")

    token_data = TokenData(user_id=user.id, email=user.email)
    token_data_serialized = json.loads(token_data.json())
    access_token = create_access_token(token_data_serialized)
    return access_token
