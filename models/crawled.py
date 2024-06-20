from typing import Any, Dict, List

import pydantic as _pydantic
from pymongo.collection import Collection


# !Crawled model
class CrawledModel(_pydantic.BaseModel):
    """Model for the crawled items in crawled collection in the database"""

    id: float
    url: str


class Crawled:
    """Crawled database collection"""

    collection: Collection[Dict[str, Any]]

    def __init__(self, collection: Collection[Dict[str, Any]]) -> None:
        self.collection = collection

    def add(self, url: str) -> Any:
        pass

    def get(self) -> List[Dict[str, str]]:
        """Get items in the crawled collection in the database"""
        return [CrawledModel(**item).model_dump() for item in self.collection.find()]

    def delete(self, item_id: float) -> None:
        """Deletes an item from the data using the id"""
        self.collection.delete_one({"id": item_id})
