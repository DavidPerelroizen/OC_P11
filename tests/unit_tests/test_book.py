import pytest

from server import book, clubs, competitions
from flask import render_template


def test_booking_with_wrong_competition_and_right_club():
    competition = "Spring Wrongstival"

    club = "Simply Lift"

    with pytest.raises(IndexError):
        book(competition, club)


def test_booking_with_right_competition_and_wrong_club():
    competition = "Spring Festival"

    club = "Simply WrongLift"

    with pytest.raises(IndexError):
        book(competition, club)


def test_booking_error_message():
    competition = "Spring Festival"

    club = "Simply WrongLift"

    with pytest.raises(IndexError):
        book(competition, club)
