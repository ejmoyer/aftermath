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
    # Room_Info is a dictionary layered as such:
    # keyname : Room(self.name, self.desc, self.unique_command, self.unique_answer)
    room_info = {
        'portal': Room('portal', # self.name - Name of Room
         """A large connecting room, with many doors on all sides leading to
        other unknown realms. In the center lies an ancient statue, it's head
        and right arm missing. It's left arm is broken off and laying to the
        side, with a small broken scale in hand.""", #self.desc - Room Description
         'examine statue, ', #self.unique_command - Unique Command for Room
          """
            The statue looks like an ancient deity worshipped by
            this realm's inhabitants. It resembles a giant humanoid, half of
            the statue being a skeleton, the other half with skin and looking
            much more human. The inscription reads 'Taviin, God of Balance'.
            """), #self.unique_answer - Unique Answer for Unique Command
        'overgrown': Room('overgrown',
         """
        The area has a huge tree in the center, with a large
        hole bored into the center of it, looks like some sort of
        energy in the middle of the hole. The rest of the area is
        overgrown and covered in roots from the large tree.""",
         'examine tree, ',
         """
            The tree seems to maintain the entire environment
            offering all the needed resources for plants to grow. However,
            there is a shaded area in the far corner of the room where
            plants are shriveled and it is noticibly colder. A skull is
            formed by the energy in the hole of the tree, maybe the tree
            is actually taking energy from the area instead?"""),
        'temple': Room('temple',
         """
        The sand dunes span for miles, this temple is deserted, but the
        sound of chanting in the distance is carried by the wind. The
        statues look like the same statue in the middle of the portal room.
        """,
         'listen closer, ',
          """
            You can hear the words 'beyond existence' in the chanting,
            perhaps the followers of the God of Balance attempted to
            ascend beyond this world somehow? Perhaps the chanting
            comes from those who accomplished their goal..
            """),
        'gate': Room('gate',
         """
        A huge atrium with many gateways, every one of them broken, unusable.
        A rusted gate is at the end of the atrium, with glyphs imprinted
        in the walls surrounding it. One of the glyphs I can translate
        says 'LIFE'.
        """,
         'approach gate, ',
          """
            The gate has an inscription..
            'In existance, only two things are in balance.
            Speak truth, and pass. Speak falsehood, and be judged.'
            ANSWER the question, or WALK away?
             """),
        'underworld': Room('underworld',
        """
        Wires span across the ceiling of this underground. The sound of
        metal moving throughout the tunnels of this area. The stench of
        death reminds you of how dangerous this area really is. A blinking
        light close to you draws your attention.
        """,
         'approach light, ',
          """
            The blinking light is attached to the body of a
            discarded robotic shell, a small broken status screen nearby
            displays 'IMBALANCE' in bright red letters.
            """)
        }

    if request.method == 'POST':
        action = request.form['action'].lower()
        g.room_name = room_name

        if action == "save":
            session['save_game'] = room_name
        elif "go to" in action:
            place = action.split( ).pop()
            return redirect(url_for(".room", room_name=place))
        elif action == "help":
            g.help = 1
        elif action in room_info[room_name].unique_command.lower():
            g.unique_command = 1
        else:
            print(1)


    return render_template('/game/room.html',
                title=room_name,
                room_description=room_info[room_name].desc,
                room_commands=room_info[room_name].unique_command + room_info[room_name].room_commands,
                unique_answer=room_info[room_name].unique_answer
                )
