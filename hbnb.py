""" Another way to run the app"""

from src import create_app
from src.config import get_config
from app import db

app = create_app(get_config())

with app.app_context():
    db.create_all()
    

if __name__ == "__main__":
    app.run()
