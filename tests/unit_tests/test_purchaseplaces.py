import flask
import pytest
from flask import Flask,render_template,request,redirect,flash,url_for, render_template_string

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


form_data = {'competition': 'Spring Festival', 'places': 4, 'club': 'Iron Temple'}


def test_buying_places_should_decrease_points_available(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    response = client.post('/purchasePlaces', json=form_data, headers=headers)

    assert ' Points available: 0' in response




def test_club_cant_buy_more_places_than_points_available():
    pass


def test_club_cant_buy_more_than_12_places():
    pass
