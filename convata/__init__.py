"""Define the flask app in this file and then import it in the file
That will serve as the main entry point for the application
"""

from flask import Flask
from .routes.fileconvert import convata_views
from .routes.otherviews import otherviews

def create_flask_app():
    """Create Flask instance and return the app object"""
    app = Flask(__name__)
    
    # Secret key for session object
    app.secret_key = "MySecretKey######$$$559686802378905"
    
    # Register blueprints of your defined routes here 
    app.register_blueprint(convata_views)
    app.register_blueprint(otherviews)
    
    return app