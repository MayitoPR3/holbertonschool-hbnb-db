from flask import Blueprint
from src.controllers.login import login

login_bp = Blueprint("login", __name__, url_prefix="/login")

login_bp.route("/", methods=["POST"])(login)