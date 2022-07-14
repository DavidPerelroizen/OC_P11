import pytest
from bs4 import BeautifulSoup
import pprint


def test_place_booking(client):

    email_for_login = {'email': 'admin@irontemple.com'}
    assertion_check = 'Welcome, admin@irontemple.com'

    response = client.post('/showSummary', data=email_for_login)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("h2")
    soup_link = soup.find_all("a")

    assert response.status_code == 200
    assert assertion_check in soup_content[0].get_text()

    response_book = client.get(soup_link[1].get('href'))
    print(response_book.headers)
    assertion_check_book = 'Iron Temple'
    assertion_check_book2 = 'Spring Festival'
    soup_book = BeautifulSoup(response_book.data, features="html.parser")
    soup_book_input = soup_book.find_all("input")

    assert assertion_check_book == soup_book_input[0].get('value')
    assert assertion_check_book2 == soup_book_input[1].get('value')
    assert response_book.status_code == 200

    places_required = 1

    form_data = {'club': soup_book_input[0].get('value'), 'competition': soup_book_input[1].get('value'),
                 'places': places_required}

    response_purchase = client.post('/purchasePlaces', data=form_data)
    assertion_check_points = 'Points available: 1'

    soup = BeautifulSoup(response_purchase.data, features="html.parser")

    assert response_purchase.status_code == 200
    assert assertion_check_points in soup.get_text()
