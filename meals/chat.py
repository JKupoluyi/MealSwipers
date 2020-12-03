from flask import Blueprint
from flask import flash
from flask import Flask
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from wtforms import Form, StringField, validators
from werkzeug.exceptions import abort

from meals.auth import login_required
from meals.db import get_db

app = Flask(__name__)
bp = Blueprint("chat", __name__, url_prefix="/chat")

class MessageForm(Form):    # Create Message Form
    body = StringField('', [validators.length(min=1)], render_kw={'autofocus': True})


@bp.route('/chatting/<id>', methods=['GET', 'POST'])
def chatting(id):
    session['lid'] = id
    uid = session.get('user_id')
    form = MessageForm(request.form)
    cur = get_db()
    users = cur.execute("SELECT * FROM user").fetchall()

    if request.method == 'POST' and form.validate():
        txt_body = form.body.data
        uid = session.get('user_id')
        db = get_db()
        db.execute("INSERT INTO messages(body, msg_by, msg_to) VALUES(?, ?, ?)",(txt_body, id, uid))
        db.commit()

    
    return render_template('chat_room.html', users=users, form=form)
   

@bp.route('/chats', methods=['GET', 'POST'])
def chats():
    print("in chats")
    id = session.get('lid')
    uid = session.get('user_id')
    cur = get_db()
    chats = cur.execute("SELECT * FROM messages WHERE (msg_by=? AND msg_to=?) OR (msg_by=? AND msg_to=?) ", (id, uid, uid, id)).fetchall()
    cur.close()
    return render_template('chats.html', chats=chats,)

