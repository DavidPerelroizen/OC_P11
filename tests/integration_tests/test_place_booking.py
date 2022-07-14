

def test_place_booking(client):

    email_for_login = {'email': 'admin@irontemple.com'}

    response = client.post('/showSummary', data=email_for_login)

    assert response.status_code == 302
    assert response.url == '/showSummary'

