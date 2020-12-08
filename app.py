from calculator.roi_calculator import calculate_odds
from matcher.match_games import match_games
from scraper.betfair.betfair_wrapper import get_list_of_betting_information_betfair
from scraper.unibet.unibet_wrapper import get_list_of_betting_information_unibet


def main() -> None:
    list_of_percentages = []
    unitbet_list = get_list_of_betting_information_unibet()
    betfair_list = get_list_of_betting_information_betfair()
    game_sets = match_games(unitbet_list, betfair_list)
    for game_pair in game_sets:
        list_of_percentages.append(calculate_odds(game_pair[0], game_pair[1]))
    print(list_of_percentages)


if __name__ == "__main__":
    main()
