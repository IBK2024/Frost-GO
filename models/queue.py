from typing import Any, Dict

import pydantic as _pydantic
from pymongo.database import Database


# !Queue input model
class QueueInput(_pydantic.BaseModel):
    url: str


# !Queue model
class Queue(QueueInput):
    id: str


# !Create a new item in the queue collection in the database
def create_queue(
    new_link: str,
    db: Database[Dict[str, Any]],
) -> Dict[str, str]:
    queue = db["queue"]
    link = QueueInput(url=new_link)

    # !Check if link already in database
    is_exist = queue.find_one({"url": link.url})
    if is_exist:
        is_exist["id"] = str(is_exist["_id"])
        result = Queue.model_validate(is_exist)
        return result.model_dump()

    inserted_id = (queue.insert_one(link.model_dump())).inserted_id
    inserted_item = link.model_dump()
    inserted_item["id"] = str(inserted_id)
    return Queue(**inserted_item).model_dump()
