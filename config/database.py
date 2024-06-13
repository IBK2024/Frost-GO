from typing import Any, Dict

from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# !Connect to database
def databaseConnect(
    mongodbURI: str,
    databaseName: str,
) -> Database[Dict[str, Any]]:
    try:
        # !Create a new client and connect to the server
        client: MongoClient[Dict[str, Any]] = MongoClient(
            mongodbURI, server_api=ServerApi("1")
        )

        # !Send a ping to confirm a successful connection to database
        client.admin.command("ping")
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        exit(0)

    return client[databaseName]
