from models.betting_model import BetInformation


def calculate_odds(betinformation1: BetInformation, betinformation2: BetInformation):
    probability1 = 1/betinformation1.player_one_odds
    probability2 = 1/betinformation2.player_two_odds
    percentage1 = (probability1+probability2)*100

    probability1 = 1/betinformation1.player_two_odds
    probability2 = 1/betinformation2.player_one_odds
    percentage2 = (probability1+probability2)*100

    if percentage1>percentage2:
        return percentage1
    return percentage2