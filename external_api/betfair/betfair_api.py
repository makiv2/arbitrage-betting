import json
from datetime import datetime

import requests

from util.config.config import get_config

config = get_config()['api']['betfair']

BETFAIR_API_URL = config['url']
BETFAIR_API_HEADERS = \
    {'X-Application': config['application_key'],
     'X-Authentication': config['session_token'],
     'content-type': 'application/json'
     }


def betfair_api_post_request(endpoint, body='{"filter":{ }}'):
    url = BETFAIR_API_URL + endpoint
    return requests.post(url, data=body, headers=BETFAIR_API_HEADERS)


def get_event_types():
    endpoint = "listEventTypes/"
    return betfair_api_post_request(endpoint)


def get_events(eventTypeId=6422):
    endpoint = "listEvents/"
    body = '{"filter":''{"eventTypeIds":''["' + str(
        eventTypeId) + '"]}}'
    return betfair_api_post_request(endpoint, body)


def get_market_types():
    endpoint = "listMarketTypes/"
    return betfair_api_post_request(endpoint)


def get_market_catalogue(eventId, max_results=100):
    endpoint = "listMarketCatalogue/"
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    body = '{"filter":{"eventIds":["' + str(
        eventId) + '"],"marketStartTime":{"from":"' + now + '"}},"sort":"FIRST_TO_START","maxResults":' + str(
        max_results) + ' }'
    return betfair_api_post_request(endpoint, body)


def get_market_book(marketId):
    endpoint = "listMarketBook/"
    body = '{"marketIds":["' + marketId + '"],"priceProjection":{"priceData":["EX_BEST_OFFERS"]}}'

    return betfair_api_post_request(endpoint, body)


def print_price_info(market_book_result):
    print('Please find Best three available prices for the runners')
    for marketBook in market_book_result:
        try:
            runners = marketBook["runners"]
            for runner in runners:
                print(runner)

                print('Selection id is ' + str(runner['selectionId']))
                if (runner['status'] == 'ACTIVE'):
                    print('Available to back price :' + str(runner['ex']['availableToBack']))
                    print('Available to lay price :' + str(runner['ex']['availableToLay']))
                else:
                    print('This runner is not active')
        except:
            print('No runners available for this market')
