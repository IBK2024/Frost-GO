from os import path
from typing import Any, Dict

from pymongo.database import Database

from general.constants import TO_PARSE_DIRECTORY
from general.createDirectory import createDirectory
from models.queue import createQueue
from setup.constants import DEFAULT_STARTING_LINK


# !Set up
def setUp(
    db: Database[Dict[str, Any]],
) -> None:

    # !Make sure toParse directory exists
    if not path.exists(TO_PARSE_DIRECTORY):
        createDirectory(TO_PARSE_DIRECTORY)

    # # !Add default starting link
    createQueue(DEFAULT_STARTING_LINK, db)
