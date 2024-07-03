# tests/test_db.py

import pytest
from app import app, db  # Import your Flask app instance and SQLAlchemy object

@pytest.fixture(scope='module')
def setup_app():
    """Fixture to set up the Flask app for testing."""
    

def test_app_creation(setup_app):
    """Test creating the Flask app."""
    assert app is not None

def test_db_creation(setup_app):
    """Test creating the SQLAlchemy db instance."""
    assert db is not None
