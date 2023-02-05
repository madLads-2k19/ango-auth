import uvicorn
from fastapi import FastAPI

from ango_auth.app.core.config import Settings

settings = Settings()

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


uvicorn.run(app, host=settings.SERVER_HOST, port=settings.SERVER_PORT)
