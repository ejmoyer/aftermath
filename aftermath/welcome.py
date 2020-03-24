from flask import (
    Blueprint, render_template, request, g, session
)

bp = Blueprint('welcome', __name__, url_prefix='/')

@bp.before_app_request
def load_previous_save():
    save_game = session.get('save_game')

    if save_game is None:
        g.save_game = None
    else:
        g.save_game = save_game

@bp.route('/')
def welcome():
    return render_template('/welcome.html')
