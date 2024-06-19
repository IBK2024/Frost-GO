from math import ceil

from fastapi import FastAPI

from crawler import Crawler
from general.constants import (
    DATABASE_NAME,
    MAX_NUMBER_OF_TREADS,
    MONGODB_URI,
    TO_PARSE_DIRECTORY,
)
from routes import router
from setup import set_up


def background_tasks() -> None:
    "Tasks to be run in the background"
    # !Connect to database
    db = set_up(MONGODB_URI, DATABASE_NAME)

    # # !Crawler
    Crawler(ceil((MAX_NUMBER_OF_TREADS / 2) * 2), TO_PARSE_DIRECTORY, db)


# !Fast API routes
app = FastAPI()
app.include_router(router)
