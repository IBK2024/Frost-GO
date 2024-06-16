from typing import Any, List

from pymongo.cursor import Cursor


# !Deserialize cursor object
def cursor_deserialize(
    cursor_object: Cursor[Any],
) -> List[Any]:
    """Deserialize cursor object gotten from mongodb"""
    return list(cursor_object)
