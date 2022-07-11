from server import showSummary
from bs4 import BeautifulSoup

clubs = [
    {
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "13"
    },
    {
        "name": "Iron Temple",
        "email": "admin@irontemple.com",
        "points": "4"
    },
    {
        "name": "She Lifts",
        "email": "kate@shelifts.co.uk",
        "points": "12"
    }]


def test_showsummary_with_good_email(client):
    form_data = {'email': 'admin@irontemple.com'}

    assertion_check = 'Welcome, admin@irontemple.com'

    response = client.post('/showSummary', data=form_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h2")

    assert assertion_check in soup_content[0].get_text()


def test_showsummary_with_wrong_email(client):
    form_data = {'email': 'test@test.com'}

    assertion_check = 'You should be redirected automatically to the target URL: '

    response = client.post('/showSummary', data=form_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("p")

    assert assertion_check in soup_content[0].get_text()


