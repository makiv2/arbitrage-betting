from typing import List

from converters.unibet_converter import UnibetConverter
from models.betting_model import BetInformation
from scraper.scraper import close_driver
from scraper.unibet.unibet_scraper import scrape_unibet, initialize_unibet_driver


def _convert_matches_to_bet_information_objects(list_of_matches) -> List[BetInformation]:
    unibet_converter = UnibetConverter()
    bet_information_list = []
    # if you get an error elements in array are shifted by one to the left, because of no day element in array 0,
    # add that in element 0 or smt
    for match in list_of_matches:
        bet_information_list.append(unibet_converter.element_to_model(match))
    return bet_information_list


def get_list_of_betting_information_unibet() -> List[BetInformation]:
    driver = initialize_unibet_driver()
    list_of_matches = scrape_unibet(driver)
    bet_information_list = _convert_matches_to_bet_information_objects(list_of_matches)
    close_driver(driver)
    return bet_information_list
