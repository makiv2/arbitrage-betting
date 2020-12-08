from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from converters.unibet_converter import UnibetConverter

def unibetscrape():
    url = "https://www.unibet.eu/betting/sports/filter/tennis"  # make it dynamic

    chrome_options = Options()  # Load chrome
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome('D:\\Betting\\arbitrage-betting\\chromedriver.exe', options=chrome_options)
    driver.get(url)

    driver.set_page_load_timeout(10)  # wait for elements to load
    list_of_events_headers = driver.find_elements_by_xpath('//header[contains(concat(" ", normalize-space(@class), " "), '
                                                           '"KambiBC-mod-event-group-header")]')

    cookie_accept_button = driver.find_element_by_id("CybotCookiebotDialogBodyButtonAccept")  # accept cookies
    cookie_accept_button.click()

    print("amount of headers", +len(list_of_events_headers))  # temporary check

    actions = ActionChains(driver)  # open headers
    iterable_of_headers = iter(list_of_events_headers)

    for header in iterable_of_headers:
        if header.text.split("\n")[0] == "Live":
            next(iterable_of_headers)
            next(iterable_of_headers)
            break
        next(iterable_of_headers)
        break

    for header in iterable_of_headers:
        actions.move_to_element(header).perform()
        header.click()

    list_of_matches = driver.find_elements_by_xpath(  # create a list of matches
        '//li[contains(concat(" ", normalize-space(@class), " "), "KambiBC-event-item--sport-TENNIS")]')

    print("amount of matches", +len(list_of_matches))  # temporary check

    unibet_converter = UnibetConverter()  #
    list_of_betinformation = []
    # if you get an error elements in array are shifted by one to the left, becasue of no day element in array 0, add dat in element 0 or smt
    for match in list_of_matches:
        list_of_betinformation.append(unibet_converter.element_to_model(match))

    print(len(list_of_betinformation))
    driver.quit()  # exit driver

    return list_of_betinformation
