"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base
from src.persistence.repository import Repository
from sqlalchemy.exc import SQLAlchemyError
from app import db

class DBRepository(Repository):
    """Dummy DB repository"""

    def __init__(self) -> None:
        """Not implemented"""
        self.session = db.session
        self.reload()
    
    def get_all(self, model_name):
        """Not implemented"""
        try:
            return self.session.query(model_name).all()
        except SQLAlchemyError:
            self.session.rollback()
            return []
        

    def get(self, model_name: str, obj_id: str):
        """Not implemented"""
        self.session.query(model_name).get(obj_id)

    def reload(self) -> None:
        """Not implemented"""
        # self.session = db.session
        db.create_all()

    def save(self, obj):
        """Not implemented"""
        self.session.add(obj)
        self.session.commit()

    def update(self, obj):
        """Not implemented"""
        self.session.commit()

    def delete(self, obj):
        """Not implemented"""
        self.session.delete(obj)
        self.session.commit()
    
"""class DataManager:
    def save(self, user):
        if app.config['USE_DATABASE']:
            db.session.add(user)
            db.session.commit()
        else:
             # Implement file-based save logic
            pass
            """