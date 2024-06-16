from os import path
from typing import Any, Dict

from pymongo.database import Database

from general.constants import TO_PARSE_DIRECTORY
from general.create_directory import create_directory
from models.queue import create_queue
from setup.constants import DEFAULT_STARTING_LINK


# !Set up the application
def set_up(
    db: Database[Dict[str, Any]],
) -> None:
    """Sets up the application"""
    # !Make sure toParse directory exists
    if not path.exists(TO_PARSE_DIRECTORY):
        create_directory(TO_PARSE_DIRECTORY)

    # # !Add default starting link
    create_queue(DEFAULT_STARTING_LINK, db)
