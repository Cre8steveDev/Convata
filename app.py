"""Entry point of the flask application"""

from convata import create_flask_app
from dotenv import load_dotenv
from os import environ
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = create_flask_app()

if __name__ == "__main__":
    app.run(debug=True)
    