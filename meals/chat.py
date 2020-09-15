from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from meals.auth import login_required
from meals.db import get_db

bp = Blueprint("chat", __name__, url_prefix="/chat")


@bp.route("/<int:id>")
def index(id):
    """Allows users to chat."""
    pass

