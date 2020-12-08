from typing import List

from converters.betfair_converter import BetfairConverter
from models.betting_model import BetInformation
from scraper.betfair.betfair_scraper import scrape_betfair, initialize_betfair_driver
from scraper.scraper import close_driver


def _convert_matches_to_bet_information_objects(list_of_matches: []) -> List[BetInformation]:
    betfair_converter = BetfairConverter()
    bet_information_list = []
    for match in list_of_matches:
        if not betfair_converter.element_to_model(match):
            continue
        bet_information_list.append(betfair_converter.element_to_model(match))
    return bet_information_list


def get_list_of_betting_information_betfair() -> List[BetInformation]:
    driver = initialize_betfair_driver()
    list_of_matches = scrape_betfair(driver)
    bet_information_list = _convert_matches_to_bet_information_objects(list_of_matches)
    close_driver(driver)
    return bet_information_list
