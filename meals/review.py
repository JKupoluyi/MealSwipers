from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from meals.auth import login_required
from meals.db import get_db

bp = Blueprint("review", __name__, url_prefix="/review")


@bp.route("/")
@login_required
def index():
    """Redirects to buy page, users are not allowed to access the index"""
    return redirect(url_for("trade.buy"))


@bp.route("/read/<string:username>", methods=("GET",))
@login_required
def read(username):
    """Shows all reviews + ratings for a specific user"""
    db = get_db()
    posts = db.execute(
        f"""
            SELECT r.timestamp, r.rating, r.description
            FROM review r
            JOIN user u ON r.seller_id = u.id
            WHERE u.username = '{username}'
            ORDER BY r.timestamp DESC
        """
    ).fetchall()
    return render_template("review/read.html", post=posts, username=username)


@bp.route("/write/<int:id>", methods=("GET", "POST"))
@login_required
def write(id):
    """Allows a user to write a review for a specific meal swipe"""
    # if the form is submitted, process it
    if request.method == "POST":
        review_star = request.form.get("star")
        review_text = request.form.get("review_text")

        error = None

        if not review_star or not review_text:
            error = "Both star and text and required"

        if error is not None:
            return "ERROR: " + error

        # return "thanks for reviewing " + str(review_star) + review_text
        else:
            db = get_db()
            meal_swipe = db.execute(
                f"""
                    SELECT m.id, username, seller_id, buyer_id
                    FROM meal_swipe m JOIN user u ON m.seller_id = u.id
                    WHERE m.id={id}
                    """
            ).fetchone()
            if not meal_swipe:
                return "ERROR: Could not find meal swipe"

            buyer_id = meal_swipe['buyer_id']
            if buyer_id != g.user['id']:
                return "ERROR: NO PERMISSION"

            db.execute(
                "INSERT INTO review (seller_id, buyer_id, swipe_id, rating, description) VALUES (?, ?, ?, ?, ?)",
                (meal_swipe['seller_id'], buyer_id, id, review_star, review_text),
            )
            db.commit()

            return redirect(url_for("review.read", username=meal_swipe['username']))

    # form is not submitted (GET request)
    # get information on the review that is trying to be written
    db = get_db()
    meal_swipe = db.execute(
        f"""
        SELECT m.id, price, timestamp_buy, username, seller_id, buyer_id
        FROM meal_swipe m JOIN user u ON m.seller_id = u.id
        WHERE m.id={id}
        """
    ).fetchone()

    error = None

    if not meal_swipe:
        error = 'Meal swipe not found'
    elif meal_swipe['buyer_id'] != g.user['id']:
        error = 'Only the buyer may write a review'

    if error is not None:
        return error
    else:
        meal_swipe = dict(meal_swipe)
        meal_swipe['timestamp_buy'] = str(meal_swipe['timestamp_buy'])[:10]
        return render_template("review/write.html", post=meal_swipe, id = id)