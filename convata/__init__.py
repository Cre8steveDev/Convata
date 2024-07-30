"""Define the flask app in this file and then import it in the file
That will serve as the main entry point for the application
"""

from flask import Flask
from .routes.fileconvert import convata_views
from .routes.otherviews import otherviews
from .routes.auth import auth

from flask_login import LoginManager
from convata.models.user_database import db, user, User
from bson import ObjectId

from dotenv import load_dotenv
from os import environ
import os

load_dotenv()


def create_flask_app():
    """Create Flask instance and return the app object"""
    
    app = Flask(__name__)
    
    # Secret key for session object
    app.secret_key = environ["APP_SECRET"]
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    
    # Store Folder path for download and uploads
    environ["DOWNLOADS"] = app.root_path + "/_DOWNLOADS"
    environ['UPLOADS'] = app.root_path + "/_UPLOADS" 
    
    # Register blueprints of your defined routes here 
    app.register_blueprint(convata_views)
    app.register_blueprint(otherviews)
    app.register_blueprint(auth)
    
    login = LoginManager(app)
    login.login_view = "/login"

    #setup the login user loader
    @login.user_loader
    def load_user(id):
        """Confirm user exists in database then use else return None"""
        cur_user = user.find_one({"_id": ObjectId(id)})
        
        if cur_user is None:
            return None
        
        # Create a user instance from the retrieved user
        return User(cur_user.get("username"), str(cur_user.get("_id")))


    return app
