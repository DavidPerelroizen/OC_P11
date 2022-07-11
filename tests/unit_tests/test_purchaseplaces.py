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

form_data = {'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': 4}


def test_buying_places_should_decrease_points_available(client):

    assertion_check = 'Great-booking complete! 4 places booked.'

    response = client.post('/purchasePlaces', data=form_data)

    soup = BeautifulSoup(response.data, features="html.parser")
    soup_content = soup.find_all("li")

    assert assertion_check in soup_content[0].get_text()


def test_club_cant_buy_more_places_than_points_available():
    pass


def test_club_cant_buy_more_than_12_places():
    pass
