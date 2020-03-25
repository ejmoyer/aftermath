from flask import (
    Blueprint, render_template, request, g, session
)

bp = Blueprint('rooms', __name__)

@bp.route('/game/<room_name>')
def room(room_name):
    return render_template('/game/room.html',
                title=room_name,
                room_description="test"
)

    routes = {
        '/portal': room('portal'),
        '/overgrown': room('overgrown'),
        '/temple': room('temple'),
        '/gate': room('gate'),
        '/underworld': room('underworld')
        }
