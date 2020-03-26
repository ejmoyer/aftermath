from flask import (
    Blueprint, render_template, request, g, session
)

bp = Blueprint('rooms', __name__)

class Room():
    room_commands = 'observe, save, change room, help'.upper()

    def __init__(self, name, desc, unique_command):
        self.name = name
        self.desc = desc
        self.unique_command = unique_command.upper()


@bp.route('/game/<room_name>', methods=('GET', 'POST'))
def room(room_name):
    descriptions = {
        'portal': Room('portal', 'I am portal', 'examine statue, '),
        'overgrown': Room('overgrown', 'I am the overgrown room.', 'examine tree, '),
        'temple': Room('temple', 'I am the temple room.', 'listen closer, '),
        'gate': Room('gate', 'I am the gate room.', 'approach gate, '),
        'underworld': Room('underworld', 'I am the underworld room.', 'approach light, ')
        }
    
    return render_template('/game/room.html',
                title=room_name,
                room_description=descriptions[room_name].desc,
                room_commands=descriptions[room_name].unique_command + descriptions[room_name].room_commands
                )
