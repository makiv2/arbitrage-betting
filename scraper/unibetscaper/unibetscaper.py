from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.unibet.eu/betting/sports/filter/tennis"   #make it dynammic!

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('D:\\Betting\\arbitrage-betting\\chromedriver.exe', options=chrome_options)
driver.get(url)
element = driver.find_elements_by_xpath('//div[contains(concat(" ", normalize-space(@class), " "), "KambiBC-mod-event-group-container")]')


for x in element:
    print(x.text)
