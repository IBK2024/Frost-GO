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
def createQueue(
    newLink: str,
    db: Database[Dict[str, Any]],
) -> Dict[str, str]:
    queue = db["queue"]
    link = QueueInput(url=newLink)

    # !Check if link already in database
    isExist = queue.find_one({"url": link.url})
    if isExist:
        isExist["id"] = str(isExist["_id"])
        result = Queue.model_validate(isExist)
        return result.model_dump()

    insertedId = (queue.insert_one(link.model_dump())).inserted_id
    insertedItem = link.model_dump()
    insertedItem["id"] = str(insertedId)
    return Queue(**insertedItem).model_dump()
