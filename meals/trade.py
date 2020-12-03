from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import session
from flask import request
from flask import url_for

from meals.auth import login_required
from meals.db import get_db

bp = Blueprint("trade", __name__)

# going to be actual homepage, swipers.com/
@bp.route("/")
def index():
    return render_template("trade/index.html")


@bp.route("/buy")
@login_required
def buy():
    """Shows all meal swipes that are available to buy"""
    """Show all the posts, most recent first."""
    db = get_db()
    meal_swipe = db.execute(
        f"""
        SELECT m.id, price, venmo, timestamp_sell, username
        FROM meal_swipe m JOIN user u ON m.seller_id = u.id
        WHERE buyer_id IS NULL
        AND m.seller_id != {g.user['id']}
        ORDER BY timestamp_sell DESC
        """
    ).fetchall()
    return render_template("trade/buy.html", posts=meal_swipe)


@bp.route("/sell", methods=("GET", "POST"))
@login_required
def sell():
    # if the form is submitted, process it
    if request.method == "POST":
        venmo = request.form["venmo"]
        price = request.form["price"]
        error = None

        if not price:
            error = "Price is required."
        
        if not venmo:
            error = "Venmo Username is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO meal_swipe (venmo, price, seller_id) VALUES (?, ?, ?)",
                (venmo, price, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("trade.buy"))

    # if user is not submitting form, display page
    return render_template("trade/sell.html")


@bp.route("/view/<int:id>", methods=("GET", "POST"))
@login_required
def view(id):
    # return information about the swipe
    db = get_db()
    post = db.execute(
        f"""
            SELECT m.id, price, venmo, timestamp_sell, username
            FROM meal_swipe m 
            JOIN user u ON m.seller_id = u.id
            WHERE m.id={id}
        """
    ).fetchone()

    review_post = db.execute(
        f"""
            SELECT r.timestamp, r.rating, r.description, b.username
            FROM meal_swipe m
            JOIN review r on m.seller_id = r.seller_id
            JOIN user b on r.buyer_id = b.id
            WHERE m.id={id}
        """
    ).fetchall()
    return render_template("trade/view.html", post=post, review_post=review_post)


