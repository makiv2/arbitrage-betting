import datetime

from converters.general_converter import Converter
from models.betting_model import BetInformation

WEBSITE_NAME = "UNIBET"


def refine_data(match) -> []:
    data = match.text.split("\n")
    if not (data[0] == "Mon" or data[0] == "Tue" or data[0] == "Wed" or data[0] == "Thu" or data[0] == "Fri" or data[0] == "Sat" or data[0] == "Sun"):
        data.insert(0, "Starting soon")
    refined_data = []
    for x in data:
        if x == "Live":
            continue
        refined_data.append(x)
    return refined_data


def get_surname(name: str) -> str:
    names = name.split(",")
    return names[0]


class UnibetConverter(Converter):
    def element_to_model(self, match) -> BetInformation:
        data = refine_data(match)
        time_of_game = data[0] + " at " + data[1]
        player_one = get_surname(data[2])
        player_two = get_surname(data[3])
        player_one_odds = float(data[6])
        player_two_odds = float(data[8])
        time_of_data = datetime.datetime.now()
        website = WEBSITE_NAME
        return BetInformation(player_one, player_two, player_one_odds, player_two_odds, time_of_game, time_of_data,
                              website)
