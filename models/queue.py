from datetime import datetime
from typing import Any, Dict, List

import pydantic as _pydantic
from pymongo.database import Database

from general.cursor_deserialize import cursor_deserialize


# !Queue input model
class QueueInput(_pydantic.BaseModel):
    """Model for the input to the queue collection in the database"""

    url: str


# !Queue model
class Queue(QueueInput):
    """Model for the queue collection in the database"""

    id: float


# !Create a new item in the queue collection in the database
def create_queue(
    new_link: str,
    db: Database[Dict[str, Any]],
) -> Dict[str, str | float]:
    """Creates an new item in the queue collection in the database"""
    queue = db["queue"]
    link = QueueInput(url=new_link)

    # !Check if link already in database if it is returns it
    is_exist = queue.find_one({"url": link.url})
    if is_exist:
        return Queue.model_validate(is_exist).model_dump()

    # !If not in database creates a new instance.
    # !Uses pydantic to validate the item to be inserted if it fails throws an error.
    insert = Queue(**link.model_dump(), id=datetime.today().timestamp()).model_dump()
    queue.insert_one(insert)

    # !Returns the inserted item
    return insert


# !Get all items in the queue collection
def get_queue(db: Database[Dict[str, Any]]) -> List[Dict[str, str | int | float]]:
    """Gets all the items in the queue collection in the database and deserialize the object"""
    return [
        Queue(**item).model_dump() for item in cursor_deserialize(db["queue"].find())
    ]


# !Deletes an item from the queue collection in the database
def delete_from_queue(
    database_item_id: float | int, db: Database[Dict[str, Any]]
) -> None:
    """Deletes an item from the queue collection in the database"""
    db["queue"].delete_one({"id": database_item_id})
