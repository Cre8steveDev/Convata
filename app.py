"""Entry point of the flask application"""

from convata import create_flask_app
from convata.models.user_database import db, user

app = create_flask_app()


if __name__ == "__main__":
    app.run(debug=True)
    