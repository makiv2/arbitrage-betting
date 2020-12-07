import datetime

from converters.general_converter import Converter
from models.betting_model import BetInformation


class UnibetConverter(Converter):
    def element_to_model(self, match):
        data = self.validate_data(match)
        time_of_game = data[0] + " at " + data[1]
        player_one = data[2]
        player_two = data[3]
        player_one_odds = data[6]
        player_two_odds = data[8]
        time_of_data = datetime.datetime.now()
        website = "unibet"
        return BetInformation(player_one, player_two, player_one_odds, player_two_odds, time_of_game, time_of_data,
                              website)


    def validate_data(self, match):
        data = match.text.split("\n")
        refined_data = []
        for x in data:
            if x == "live":
                continue
            refined_data.append(x)
        return refined_data






