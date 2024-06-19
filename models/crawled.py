from typing import Any, Dict, List

import pydantic as _pydantic
from pymongo.database import Database

from general.cursor_deserialize import cursor_deserialize


# !Crawled input model
class CrawledInput(_pydantic.BaseModel):
    """Model for the input to the crawled collection in the database"""

    url: str


# !Crawled model
class Crawled(CrawledInput):
    """Model for the crawled collection in the database"""

    id: float


# !Create a new item in the crawled collection in the database
def create_crawled() -> None:
    """Creates an new item in the crawled collection in the database"""


# !Get all items in the crawled collection
def get_crawled(db: Database[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Gets all the items in the crawled collection in the database"""
    # !Validates the data received from the database
    return [
        Crawled(**item).model_dump()
        for item in cursor_deserialize(db["crawled"].find())
    ]


# !Deletes an item from the crawled collection in the database
def delete_from_crawled(
    database_item_id: float | int, db: Database[Dict[str, Any]]
) -> None:
    """Deletes an item from the crawled collection in the database"""
    db["crawled"].delete_one({"id": database_item_id})
