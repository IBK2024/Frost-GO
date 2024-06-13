from fastapi import FastAPI

from config.database import database_connect
from general.constants import DATABASE_NAME, MONGODB_URI
from routes.routes import router
from setup.setup import set_up

# !Connect to database
db = database_connect(MONGODB_URI, DATABASE_NAME)

# !Setup
set_up(db)

# !Fast Api
app = FastAPI()
app.include_router(router)
