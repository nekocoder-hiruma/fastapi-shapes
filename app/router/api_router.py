from fastapi import APIRouter

from app.constants import error_responses
from app.router import auth, user, shapes

api_router = APIRouter()

api_router.include_router(router=auth.router,
                          tags=["login"],
                          responses=error_responses("User"))
api_router.include_router(router=user.router,
                          prefix="/users",
                          tags=["users"],
                          responses=error_responses("User"))
api_router.include_router(router=shapes.router,
                          prefix="/shapes",
                          tags=["shapes"],
                          responses=error_responses("Shapes"))
