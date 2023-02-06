from urllib.parse import urljoin

import requests
from pydantic import EmailStr

from ango_auth.app.core.config import Settings
from ango_auth.app.models.user import UserDb

settings = Settings()


def get_user_details(email: EmailStr) -> UserDb:
    url = urljoin(settings.APP_DOMAIN, f"user/v1/{email}")
    cookies = {"shared_secret": settings.SHARED_ACCESS_TOKEN}
    resp = requests.get(url, cookies=cookies)
    user = UserDb.parse_obj(resp.json())
    return user
