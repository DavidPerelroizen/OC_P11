import pytest
from flask import Flask,render_template,request,redirect,flash,url_for, json
from bs4 import BeautifulSoup
import requests
from werkzeug.datastructures import MultiDict, ImmutableMultiDict

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

competitions: [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]


def test_buying_places_should_decrease_points_available(client):
    form_data = {'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 1}

    assertion_check = 'Points available: 1'

    response = client.post('/purchasePlaces', data=form_data)

    soup = BeautifulSoup(response.data, features="html.parser")

    assert assertion_check in soup.get_text()


def test_club_cant_buy_more_places_than_points_available(client):
    form_data = {'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 5}

    assertion_check = 'Sorry you can\'t order more places than you have points available'

    response = client.post('/purchasePlaces', data=form_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("li")

    assert assertion_check in soup_content[0].get_text()


def test_club_cant_buy_more_than_12_places(client):
    form_data = {'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 14}

    assertion_check = 'Sorry you can\'t order more than 12 places for an event'

    response = client.post('/purchasePlaces', data=form_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("li")

    assert assertion_check in soup_content[0].get_text()


def test_club_cant_buy_more_places_than_available_for_competition(client):
    form_data = {'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 30}

    assertion_check = 'Sorry you can\'t order more places than what is available for this competition'

    response = client.post('/purchasePlaces', data=form_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("li")

    assert assertion_check in soup_content[0].get_text()
