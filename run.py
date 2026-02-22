"""Entry point: create the Flask app and run the development server."""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
