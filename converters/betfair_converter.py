import datetime


from converters.general_converter import Converter
from models.betting_model import BetInformation


def validate_data(match):
    data = match.text.split("\n")
    refined_data = []
    for x in data:
        if x == "SUSPENDED" or x == 'CLOSED':
            return False
        refined_data.append(x)
    if len(data[0]) == 1 and len(data[1]) == 1 and len(data[2]) == 1 and len(data[3]) == 1:
        return False
    return refined_data


def optimize_name(name):
    names = name.split(" ")
    return names[1]


class BetfairConverter(Converter):
    def element_to_model(self, match):
        data = validate_data(match)
        print(data)
        if not data:
            return False
        time_of_game = data[0]
        player_one = optimize_name(data[4])
        player_two = optimize_name(data[5])
        player_one_odds = float(data[1])
        player_two_odds = float(data[2])
        time_of_data = datetime.datetime.now()
        website = "betfair"

        return BetInformation(player_one, player_two, player_one_odds, player_two_odds, time_of_game, time_of_data,
                              website)
