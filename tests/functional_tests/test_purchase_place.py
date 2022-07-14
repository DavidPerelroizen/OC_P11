from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_purchase_places():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5000/')

    assert chrome_driver.current_url == 'http://127.0.0.1:5000/'

    email_input = chrome_driver.find_element(by=By.ID, value="email")
    email_input.send_keys("admin@irontemple.com")
    enter_button = chrome_driver.find_element(by=By.TAG_NAME, value="button")
    enter_button.click()

    assert chrome_driver.current_url == 'http://127.0.0.1:5000/showSummary'
    assert "Welcome, admin@irontemple.com" in chrome_driver.page_source

    book_places = chrome_driver.find_elements(by=By.TAG_NAME, value="a")
    book_places[1].click()

    assert 'Spring Festival' in chrome_driver.page_source

    places_to_book = chrome_driver.find_element(By.NAME, "places")
    places_to_book.send_keys(1)
    book_button = chrome_driver.find_element(by=By.TAG_NAME, value="button")
    book_button.click()

    assert 'Great-booking complete! 1 places booked.' in chrome_driver.page_source
    assert 'Points available: 1' in chrome_driver.page_source

    links = chrome_driver.find_elements(by=By.TAG_NAME, value="a")
    links[0].click()

    assert chrome_driver.current_url == 'http://127.0.0.1:5000/'

    chrome_driver.close()

