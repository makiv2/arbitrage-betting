from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from scraper.scraper import get_web_driver, implicit_wait, get_explicit_wait, close_driver
from util.config.config import get_config

config = get_config()['betfair']


def _accept_cookie(driver: WebDriver) -> None:
    wait = get_explicit_wait(driver, 15, 1, [NoSuchElementException])
    visible_cookie_accept_button = wait.until(element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    visible_cookie_accept_button.click()


def _get_list_of_matches(driver: WebDriver) -> []:
    return driver.find_elements_by_xpath('//li[contains(concat(" ", normalize-space(@class), " "), '
                                         '"com-coupon-line-new-layout")]')


def initialize_betfair_driver():
    return get_web_driver(config['url'])


# Scrape betfair for matches
# @return list of found matches
def scrape_betfair(driver: WebDriver) -> []:
    list_of_matches = []
    try:
        implicit_wait(driver, 10)  # wait for elements to load
        _accept_cookie(driver)
        list_of_matches = _get_list_of_matches(driver)
    except Exception as e:
        print(e)
        close_driver(driver)
    return list_of_matches
