from typing import List

from models.betting_model import BetInformation


def match_games(betinformation1: List[BetInformation], betinformation2: List[BetInformation]):
    list_of_matched_games = []
    for match1 in betinformation1:
        for match2 in betinformation2:
            if match1.player_one in match2.player_one:
                list_of_matched_games.append([match1,match2])
                print(match1.player_one)
            if match1.player_two in match2.player_two:
                if [match1, match2] in list_of_matched_games:
                    continue
                list_of_matched_games.append([match1, match2])
    print(list_of_matched_games)
    return list_of_matched_games
