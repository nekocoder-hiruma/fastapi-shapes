from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from app import config
from app.database.db import SessionLocal
from app.router.api_router import api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

app.include_router(api_router, prefix=f"api/{config.API_VERSION}")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal Server Error",
                        status_code=HTTP_500_INTERNAL_SERVER_ERROR)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
