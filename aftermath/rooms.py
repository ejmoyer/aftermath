from flask import (
    Blueprint, render_template, request, g, session, redirect, url_for
)

bp = Blueprint('rooms', __name__)

class Room():
    def __init__(self, name, desc, unique_command, unique_answer):
        self.name = name
        self.desc = desc
        self.unique_command = unique_command.upper()
        self.unique_answer = unique_answer
        self.room_commands = 'save, go to (room name), help'.upper()

@bp.route('/game/<room_name>', methods=('GET', 'POST'))
def room(room_name):
    descriptions = {
        'portal': Room('portal', """A large connecting room, with many doors on all sides leading to
        other unknown realms. In the center lies an ancient statue, it's head
        and right arm missing. It's left arm is broken off and laying to the
        side, with a small broken scale in hand.""", 'examine statue, ', 'test'),
        'overgrown': Room('overgrown', """
        The area has a huge tree in the center, with a large
        hole bored into the center of it, looks like some sort of
        energy in the middle of the hole. The rest of the area is
        overgrown and covered in roots from the large tree.""", 'examine tree, ', 'test'),
        'temple': Room('temple', 'I am the temple room.', 'listen closer, ', 'test'),
        'gate': Room('gate', 'I am the gate room.', 'approach gate, ', 'test'),
        'underworld': Room('underworld', 'I am the underworld room.', 'approach light, ', 'test')
        }

    if request.method == 'POST':
        action = request.form['action'].lower()

        if action == "save":
            session['save_game'] = room_name
        elif "go to" in action:
            place = action.split( ).pop()
            return redirect(url_for(".room", room_name=place))
        elif action == "help":
            g.help = 1
            print(descriptions[room_name].unique_command)
        elif action in descriptions[room_name].unique_command.lower():
            g.unique_command = 1
        else:
            print('no')

    return render_template('/game/room.html',
                title=room_name,
                room_description=descriptions[room_name].desc,
                room_commands=descriptions[room_name].unique_command + descriptions[room_name].room_commands,
                unique_answer=descriptions[room_name].unique_answer
                )
