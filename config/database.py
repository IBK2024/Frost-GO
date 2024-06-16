from typing import Any, Dict

from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# !Connect to database
def database_connect(
    mongodb_uri: str,
    database_name: str,
) -> Database[Dict[str, Any]]:
    """
    Connect to database.

    Also send a ping to confirm successful connection.
    """

    # !Create a new client and connect to the server
    client: MongoClient[Dict[str, Any]] = MongoClient(
        mongodb_uri, server_api=ServerApi("1")
    )

    # !Send a ping to confirm a successful connection to database
    client.admin.command("ping")
    print("Successfully connected to MongoDB!")

    # !Return client
    return client[database_name]
