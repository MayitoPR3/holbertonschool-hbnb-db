from flask import Blueprint
from src.controllers.login import admin_data, login, protected, test

login_bp = Blueprint("login", __name__, url_prefix="/login")
protected_bp = Blueprint("protected", __name__, url_prefix="/protected")
admin_data_bp = Blueprint("admin_data", __name__, url_prefix="/admin/data")

test_bp = Blueprint("test", __name__, url_prefix="/test")

login_bp.route('/', methods=["POST"])(login)
protected_bp.route("/", methods=["GET"])(protected)
admin_data_bp.route("/", methods=['POST', 'DELETE'])(admin_data)

# Just a route created for testing purposes
test_bp.route("/", methods=['GET'])(test)