from external_api.betfair.betfair_api import betfair_api_post_request


def main():
    response = betfair_api_post_request("/listEventTypes/")
    print(response.text)


if __name__ == "__main__":
    main()