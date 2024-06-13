from fastapi import FastAPI

from config.database import databaseConnect
from general.constants import DATABASE_NAME, MONGODB_URI
from routes.routes import router
from setup.setup import setUp

# !Connect to database
db = databaseConnect(MONGODB_URI, DATABASE_NAME)

# !Setup
setUp(db)

# !Fast Api
app = FastAPI()
app.include_router(router)
