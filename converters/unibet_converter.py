import datetime

from converters.general_converter import Converter
from models.betting_model import BetInformation


def validate_data(match):
    data = match.text.split("\n")
    refined_data = []
    for x in data:
        if x == "Live":
            continue
        refined_data.append(x)
    return refined_data

def optimize_name(name):
    names = name.split(",")
    return names[0]


class UnibetConverter(Converter):
    def element_to_model(self, match):
        data = validate_data(match)
        time_of_game = data[0] + " at " + data[1]
        player_one = optimize_name(data[2])
        player_two = optimize_name(data[3])
        player_one_odds = float(data[6])
        player_two_odds = float(data[8])
        time_of_data = datetime.datetime.now()
        website = "unibet"
        return BetInformation(player_one, player_two, player_one_odds, player_two_odds, time_of_game, time_of_data,
                              website)
