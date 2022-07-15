from selenium import webdriver
from selenium.webdriver.common.by import By


def test_authentication():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('http://127.0.0.1:5000/')

    assert chrome_driver.current_url == 'http://127.0.0.1:5000/'

    email_input = chrome_driver.find_element(by=By.ID, value="email")
    email_input.send_keys("admin@irontemple.com")
    enter_button = chrome_driver.find_element(by=By.TAG_NAME, value="button")
    enter_button.click()

    assert chrome_driver.current_url == 'http://127.0.0.1:5000/showSummary'
    assert "Welcome, admin@irontemple.com" in chrome_driver.page_source

    chrome_driver.close()
