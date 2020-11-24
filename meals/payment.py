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

import datetime


bp = Blueprint("payment", __name__, url_prefix="/payment")


@bp.route("/")
@login_required
def index():
    """Redirects to buy page, users are not allowed to access the index"""
    return redirect(url_for("trade.buy"))


@bp.route("/<int:id>/buy", methods=("GET",))
@login_required
def buy(id):
    """Processes payment for swipe"""
    db = get_db()
    db.execute(
        f"""
        UPDATE meal_swipe
        SET buyer_id = {g.user['id']}, timestamp_buy = '{datetime.datetime.now()}'
        WHERE id={id}
        """
    )
    db.commit()

    db = get_db()
    
    ms = db.execute(
        f"""select * from meal_swipe
            WHERE id = {id}
        """
    ).fetchone()

    for row in db.execute('select * from meal_swipe'):
        print(dict(row))

    ms = dict(ms)
    for key, value in ms.items():
        print("This is the one fetched record")
        print(key, value)
    print(ms['timestamp_sell'])

    return render_template("payment/viewpayment.html", post=ms)


@bp.route("/<int:id>/get_paid", methods=("GET", "POST"))
@login_required
def sell(id):
    """Allows sellers to claim payment for a confirmed + completed transaction"""
    pass

"""
@bp.route("/viewp", methods=("GET",))
@login_required
def view():
    return render_template("payment/pay.html", post = g.user)

"""

@bp.route("/viewp/<int:id>", methods=("GET", "POST"))
@login_required
def view(id):
    print(id)
    """Update a post if the current user is the author."""
    # user has clicked 'buy'
    # if request.method == "POST":
    #     # todo: change everything within if
    #     title = request.form["title"]
    #     body = request.form["body"]
    #     error = None
    #
    #     if not title:
    #         error = "Title is required."
    #
    #     if error is not None:
    #         flash(error)
    #     else:
    #         db = get_db()
    #         db.execute(
    #             "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
    #         )
    #         db.commit()
    #         return redirect(url_for("payment.buy"))

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
    return render_template("payment/pay.html", post=post, review_post=review_post)


