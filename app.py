import json

from external_api.betfair.betfair_api import betfair_api_post_request, get_market_catalogue, get_market_types, \
    get_events, get_market_book, print_price_info, list_runner_book


def main():
    response = get_events()
    #print(json.dumps(json.loads(response.text), indent=3))
    response = get_market_catalogue("30169676")
    print(json.dumps(json.loads(response.text), indent=3))
    response = get_market_book("1.176479557")
    #print(json.dumps(json.loads(response.text), indent=3))

    #response1 = print_price_info(json.loads(response.text))

    response2 = list_runner_book("1.176479557", "2278790")
    #print(json.dumps(json.loads(response2.text), indent=3))

if __name__ == "__main__":
    main()
