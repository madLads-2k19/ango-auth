import uvicorn
from fastapi import FastAPI

from ango_auth.app.core.config import Settings
from ango_auth.app.routers.auth import auth_router

settings = Settings()

app = FastAPI(
    title="Ango - Authentication microservice",
    docs_url=f"{settings.APP_PREFIX.rstrip('/')}/docs",
    redoc_url=f"{settings.APP_PREFIX.rstrip('/')}/redoc",
    openapi_url=f"{settings.APP_PREFIX.rstrip('/')}/openapi.json",
)

app.include_router(auth_router, prefix=f"{settings.APP_PREFIX.rstrip('/')}/v1", tags=["Auth API V1"])

if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
