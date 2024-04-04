"""Entry point of the flask application"""

from convata import create_flask_app

app = create_flask_app()

if __name__ == "__main__":
    app.run(debug=True)
    