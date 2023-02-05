import uvicorn
from fastapi import FastAPI

from ango_auth.app.core.config import Settings
from ango_auth.app.routers.auth import auth_router

settings = Settings()

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


app.include_router(auth_router, prefix="/auth")

uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
