from fastapi import FastAPI
from fastapi.routing import APIRouter
from routers.routers import routers
from config import settings

def init_app(app: FastAPI):
    router = APIRouter(prefix=settings.URL_PREFIX)
    for r in routers:
        router.include_router(r)
    app.include_router(router)