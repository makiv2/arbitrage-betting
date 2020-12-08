from calculator.roicalculator import calculate_odds
from matcher.match_games import match_games
from scraper.betfairscraper.betfairscraper import betfairscrape
from scraper.unibetscaper.unibetscaper import unibetscrape


def main():
    list_of_percentages = []
    unitbet_list = unibetscrape()
    betfair_list = betfairscrape()
    game_sets = match_games(unitbet_list,betfair_list)
    for game_pair in game_sets:
        list_of_percentages.append(calculate_odds(game_pair[0], game_pair[1]))
    print(list_of_percentages)

if __name__ == "__main__":
    main()
