from server import loadCompetitions


def test_loadcompetitions_should_return_competitions_list():
    expected_value = [
        {
            "name": "Spring Festival",
            "date": "2022-07-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2022-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
    assert loadCompetitions() == expected_value
