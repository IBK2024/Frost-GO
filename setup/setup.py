from os import path
from typing import Any, Dict

from pymongo.database import Database

from config.database import database_connect
from general.constants import TO_PARSE_DIRECTORY
from general.create_directory import create_directory
from models.queue import create_queue
from setup.constants import DEFAULT_STARTING_LINK


# !Set up the application
def set_up(mongodb_uri: str, database_name: str) -> Database[Dict[str, Any]]:
    """Sets up the application"""
    db = database_connect(
        mongodb_uri,
        database_name,
    )

    # !Make sure toParse directory exists
    if not path.exists(TO_PARSE_DIRECTORY):
        create_directory(TO_PARSE_DIRECTORY)

    # # !Add default starting link
    create_queue(DEFAULT_STARTING_LINK, db)

    return db
