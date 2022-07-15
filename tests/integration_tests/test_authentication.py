from bs4 import BeautifulSoup


def test_authentication(client):

    email_for_login = {'email': 'admin@irontemple.com'}
    assertion_check = 'Welcome, admin@irontemple.com'

    response = client.post('/showSummary', data=email_for_login)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h2")

    assert response.status_code == 200
    assert assertion_check in soup_content[0].get_text()

    response_logout = client.get('/logout')

    assert response_logout.status_code == 302
