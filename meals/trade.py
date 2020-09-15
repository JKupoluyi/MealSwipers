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

bp = Blueprint("trade", __name__)

# going to be actual homepage, swipers.com/
@bp.route("/")
def index():
    return render_template("trade/index.html")


@bp.route("/buy", methods=("GET",))
@login_required
def buy():
    """Shows all meal swipes that are available to buy"""
    db = get_db()
    posts = db.execute(
        # todo: make query
    ).fetchall()
    return render_template("trade/buy.html", posts=posts)


@bp.route("/sell", methods=("GET", "POST"))
@login_required
def sell():
    # if the form is submitted, process it
    if request.method == "POST":
        # todo: change everything within if
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
                (title, body, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("trade.buy"))

    # if user is not submitting form, display page
    return render_template("trade/sell.html")


@bp.route("/<int:id>/view", methods=("GET", "POST"))
@login_required
def view(id):
    """Update a post if the current user is the author."""

    # user has clicked 'buy'
    if request.method == "POST":
        # todo: change everything within if
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
            )
            db.commit()
            return redirect(url_for("payment.buy"))

    # return information about the swipe
    post = {}
    return render_template("trade/view.html", post=post)