import aftermath

def test_welcome(client):
    response = client.get('/')
    assert response
    assert b'href="/game/portal"' in response.data
