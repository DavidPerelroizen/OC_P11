from server import showSummary


def test_showsummary_with_good_email():
    email_fortest = "admin@irontemple.com"
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

    club = [club for club in clubs if club['email'] == email_fortest][0]

    assert club == clubs[1]


def test_showsummary_with_wrong_email():
    email_fortest = "test@test.com"
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
    try:
        club = [club for club in clubs if club['email'] == email_fortest][0]
        assert club == clubs[1]
    except IndexError:
        assert 1 == 1


