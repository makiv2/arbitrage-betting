from typing import List, Iterator

from selenium.webdriver import ActionChains
from selenium.webdriver.android.webdriver import WebDriver

from scraper.scraper import get_web_driver, implicit_wait, close_driver
from util.config.config import get_config

config = get_config()['unibet']


# @return iterable of event headers
def _get_event_headers(driver: WebDriver) -> Iterator:
    list_of_event_headers = driver.find_elements_by_xpath(
        '//header[contains(concat(" ", normalize-space(@class), " "), '
        '"KambiBC-mod-event-group-header")]')
    return iter(list_of_event_headers)


def _accept_cookie(driver: WebDriver) -> None:
    cookie_accept_button = driver.find_element_by_id("CybotCookiebotDialogBodyButtonAccept")
    cookie_accept_button.click()


# TODO: optimize this
def _open_event_headers(driver: WebDriver, event_headers: Iterator) -> None:
    actions = ActionChains(driver)
    for header in event_headers:
        if header.text.split("\n")[0] == "Live":
            next(event_headers)
            next(event_headers)
            break
        next(event_headers)
        break
    for header in event_headers:
        actions.move_to_element(header).perform()
        header.click()


def _get_list_of_matches(driver: WebDriver) -> []:
    return driver.find_elements_by_xpath(
        '//li[contains(concat(" ", normalize-space(@class), " "), "KambiBC-event-item--sport-TENNIS")]')


def initialize_unibet_driver():
    return get_web_driver(config['url'])


# Scrape unibet for matches
# @return list of matches
def scrape_unibet(driver: WebDriver) -> []:
    list_of_matches = []
    try:
        implicit_wait(driver, 10)  # wait for elements to load
        _accept_cookie(driver)
        event_headers = _get_event_headers(driver)
        _open_event_headers(driver, event_headers)
        list_of_matches = _get_list_of_matches(driver)
    except Exception as e:
        print(e)
        close_driver(driver)
    return list_of_matches
