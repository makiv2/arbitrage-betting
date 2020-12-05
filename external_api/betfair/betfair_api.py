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



# print(json.dumps(json.loads(response.text), indent=3))