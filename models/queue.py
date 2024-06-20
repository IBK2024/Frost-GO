from datetime import datetime
from typing import Any, Dict, List

import pydantic as _pydantic
from pymongo.collection import Collection


# !Queue model
class QueueModel(_pydantic.BaseModel):
    """Model for the queue items in queue collection in the database"""

    id: float
    url: str


class Queue:
    """Queue database collection"""

    collection: Collection[Dict[str, Any]]

    def __init__(self, collection: Collection[Dict[str, Any]]) -> None:
        self.collection = collection

    def add(self, url: str) -> Dict[str, Any]:
        """Creates a new item in the queue collection in the database"""
        link = QueueModel(id=datetime.today().timestamp(), url=url)

        # !Check if link already in database if it is returns it
        is_exist = self.collection.find_one({"url": link.url})
        if is_exist:
            return QueueModel(**is_exist).model_dump()

        # !If not in database creates a new instance.
        self.collection.insert_one(link.model_dump())

        # !Returns the inserted item
        return link.model_dump()

    def get(self) -> List[Dict[str, str | float]]:
        """Get items in the queue collection in the database"""
        return [QueueModel(**item).model_dump() for item in self.collection.find()]

    def delete(self, item_id: float) -> None:
        """Deletes an item from the data using the id"""
        self.collection.delete_one({"id": item_id})
