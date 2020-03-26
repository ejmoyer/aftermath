from aftermath import rooms

def test_rooms(client):
    rooms = {
    'resp_portal': client.get('/game/portal'),
    'resp_gate': client.get('/game/gate'),
    'resp_overgrown': client.get('/game/overgrown'),
    'resp_temple': client.get('/game/temple'),
    'resp_underworld': client.get('/game/underworld')
    }

    for room in rooms:
        response = rooms.get(room)
        assert response
        assert b'You are in' in response.data
        assert b'My surroundings are' in response.data
        assert b'Should I' in response.data
        assert b'<form method="post">' in response.data
