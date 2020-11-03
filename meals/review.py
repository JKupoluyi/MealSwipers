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
    # db = get_db()
    # posts = db.execute(
    #     # todo: make query
    # ).fetchall()
    post = {}
    return render_template("review/read.html", post=post, username=username)


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

            # todo: delete once buying is available
            buyer_id = meal_swipe['buyer_id']
            if not buyer_id:
                buyer_id = 0

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
    # todo: reenable once buying is active
    # elif meal_swipe['buyer_id'] != logged_in_user_id:
    #     error = 'Only the buyer may write a review'

    if error is not None:
        return error
    else:
        return render_template("review/write.html", post=meal_swipe)