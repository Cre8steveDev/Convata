from os import environ
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from werkzeug.security import check_password_hash


# Create a new client and connect to the server
URI = environ["MONGO_URI"]

client = MongoClient(f"{URI}=true&w=majority&appName=Cre8steveDatabase", server_api=ServerApi('1'))

# Access a database from the client 
db = client["Cre8steveDatabase"]

print("=====================================")
print("Database Access established!")
print("=====================================")

user = db["Users"] # type: ignore


# Define Class to use to map Mongodb Data for user login
class User:
    """Class Definition to handle Flask login for user"""
    def __init__(self, username, id):
        self.username = username
        self.id = id
    
    @staticmethod 
    def is_authenticated():
        return True
    
    @staticmethod
    def is_active():
        return True
    
    @staticmethod
    def is_anonymous():
        return False
    
    def get_id(self):
        return self.id
