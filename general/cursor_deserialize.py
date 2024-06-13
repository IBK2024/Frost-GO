from typing import Any, List

from pymongo.cursor import Cursor


# !Deserialize cursor object
def cursor_deserialize(
    cursor: Cursor[Any],
) -> List[Any]:
    result: List[Any] = []
    for item in cursor:
        result.append(item)
    return result
