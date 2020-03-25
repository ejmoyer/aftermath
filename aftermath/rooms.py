from flask import (
    Blueprint, render_template, request, g, session
)

bp = Blueprint('rooms', __name__)

@bp.route('/game/<room_name>')
def room(room_name):
    descriptions = {
        'portal': 'I am the portal room.', #maybe make these objects with more info?
        'overgrown': 'I am the overgrown room.',
        'temple': 'I am the temple room.',
        'gate': 'I am the gate room.',
        'underworld': 'I am the underworld room.'
        }

    return render_template('/game/room.html',
                title=room_name,
                room_description=descriptions[room_name]
                )
