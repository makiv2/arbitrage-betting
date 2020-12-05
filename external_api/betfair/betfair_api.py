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


def get_events(eventTypeId=2):
    endpoint = "listEvents/"
    body = '{"filter":''{"eventTypeIds":''["' + str(
        eventTypeId) + '"]}}'
    return betfair_api_post_request(endpoint, body)


def get_market_catalogue(eventTypeId=2, max_results=1000):
    endpoint = "listMarketCatalogue/"
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    body = '{"filter":''{"eventTypeIds":''["' + str(
        eventTypeId) + '"],"marketStartTime":{"from":"' + now + '"}}, "maxResults":"' + str(max_results) + '}'
    return betfair_api_post_request(endpoint, body)


def get_market_types():
    endpoint = "listMarketTypes/"
    return betfair_api_post_request(endpoint)


def get_market_book():
    endpoint = "listMarketBook/"
