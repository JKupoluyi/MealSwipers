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
        'select * from meal_swipe'
    ).fetchone()

    # ms = dict(ms)
    # for key, value in ms.items():
    #     print(key, value)
    # print(ms['timestamp_sell'])

    return "<p>YOU HAVE JUST BOUGHT MEAL SWIPE ID " + str(id) + f"</p><p>CLICK TO WRITE A REVIEW <a href='{url_for('review.write', id=id)}'>HERE</a> HELLO"


@bp.route("/<int:id>/get_paid", methods=("GET", "POST"))
@login_required
def sell(id):
    """Allows sellers to claim payment for a confirmed + completed transaction"""
    pass