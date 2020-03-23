from flask import (
    Blueprint, render_template, request
)

bp = Blueprint('welcome', __name__, url_prefix='/welcome')

@bp.route('/welcome', methods=('GET'))
def welcome():
    return render_template('/welcome.html')
