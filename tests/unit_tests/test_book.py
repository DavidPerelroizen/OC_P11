import pytest

from server import book, clubs, competitions
from flask import render_template
from .conftest import client
from bs4 import BeautifulSoup


def test_booking_with_wrong_competition_and_right_club(client):
    competition = "Spring wrongFestival"

    club = "Simply Lift"

    assertion_check = 'Something went wrong-please try again'

    response = client.get('/book/' + competition + '/' + club)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("li")

    assert assertion_check in soup_content[0].get_text()


def test_booking_with_right_competition_and_wrong_club(client):
    competition = "Spring Festival"

    club = "Simply WrongLift"

    assertion_check = 'Something went wrong-please try again'

    response = client.get('/book/' + competition + '/' + club)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("li")

    assert assertion_check in soup_content[0].get_text()

def test_booking_error_message(client):
    competition = "Spring Festival"
    club = "Simply WrongLift"
    assertion_check = 'Something went wrong-please try again'

    response = client.get('/book/' + competition + '/' + club)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("li")

    assert assertion_check in soup_content[0].get_text()


def test_booking_route(client):
    competition = "Spring Festival"

    club = "Simply WrongLift"

    response = client.get('/book/'+competition+'/'+club)

    assert response.status_code == 200
