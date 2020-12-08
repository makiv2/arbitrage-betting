from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from converters.betfair_converter import BetfairConverter


def betfairscrape():
    url = "https://www.betfair.com/sport/tennis"  # make it dynamic

    chrome_options = Options()  # Load chrome
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome('D:\\Betting\\arbitrage-betting\\chromedriver.exe', options=chrome_options)
    driver.get(url)

    driver.set_page_load_timeout(10)  # wait for elements to load

    wait = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[NoSuchElementException])  # accept cookies
    visible_cookie_accept_button = wait.until(element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    visible_cookie_accept_button.click()

    list_of_matches = driver.find_elements_by_xpath('//li[contains(concat(" ", normalize-space(@class), " "), '
                                                    '"com-coupon-line-new-layout")]')

    print("amount of matches", +len(list_of_matches))  # temporary check

    betfair_converter = BetfairConverter()  # Convert matches to betinformation
    list_of_betinformation = []
    for match in list_of_matches:
        if not betfair_converter.element_to_model(match):
            continue
        list_of_betinformation.append(betfair_converter.element_to_model(match))

    print(len(list_of_betinformation))

    driver.quit()  # exit driver

    return list_of_betinformation
