from typing import List

from models.betting_model import BetInformation


# TODO: optimize
def match_games(betinformation1: List[BetInformation], betinformation2: List[BetInformation]):
    list_of_matched_games = []
    for match1 in betinformation1:
        for match2 in betinformation2:
            if match1.player_one in match2.player_one:
                list_of_matched_games.append([match1, match2])
            if match1.player_two in match2.player_two:
                if [match1, match2] in list_of_matched_games:
                    continue
                list_of_matched_games.append([match1, match2])
    return list_of_matched_games
