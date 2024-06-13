from os import getenv

from dotenv import load_dotenv

PATH_TO_ENV = "./env/.env"

# !Load env file
load_dotenv(PATH_TO_ENV)

# !Env object
ENV = {"MONGODB_URI": getenv("MONGODB_URI", "mongodb://localhost:27017/")}
