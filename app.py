import json

from external_api.betfair.betfair_api import betfair_api_post_request, get_market_catalogue, get_market_types, \
    get_events


def main():
    response = get_events()
    print(json.dumps(json.loads(response.text), indent=3))


if __name__ == "__main__":
    main()
