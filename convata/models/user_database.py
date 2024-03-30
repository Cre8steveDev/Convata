from os import environ
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.database import Database


# Create a new client and connect to the server
client = MongoClient(environ["MONGO_URI"], server_api=ServerApi('1'))

# Access a database from the client 
db = client ["Cre8steveDatabase"]
user = db["Users"] # type: ignore

