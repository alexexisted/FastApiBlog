from fastapi import FastAPI
from backend.core.config import settings
from backend.db.base import Base
from backend.db.session import engine

from fastapi.staticfiles import StaticFiles
import os

from backend.apis.base import api_router
from backend.apps.base import app_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(app_router)


def configure_staticfiles(app):
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    app.mount("/static",
              StaticFiles(directory=static_dir),
              name="static")


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    configure_staticfiles(app)
    return app


app = start_application()


@app.get("/")
def home():
    return {"msg":"Hello FastAPI"}


