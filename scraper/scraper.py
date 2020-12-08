from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from util.path.path import get_abs_path

CHROMEDRIVER_ABS_PATH = "chromedriver/chromedriver.exe"


def get_web_driver(url: str) -> WebDriver:
    driver = None
    try:
        driver = webdriver.Chrome(get_abs_path(CHROMEDRIVER_ABS_PATH), options=_get_chrome_options())
        driver.get(url)
        return driver
    except Exception as e:
        driver.close()
        print(e)


def implicit_wait(driver: WebDriver, time_in_seconds: int) -> None:
    driver.set_page_load_timeout(time_in_seconds)


def get_explicit_wait(driver: WebDriver, max_wait_time: int, poll_freq: int, ignored_exceptions: []) -> WebDriverWait:
    return WebDriverWait(driver, max_wait_time, poll_frequency=poll_freq, ignored_exceptions=ignored_exceptions)


def _get_chrome_options() -> Options:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    return chrome_options


def close_driver(driver: WebDriver) -> None:
    driver.close()


def quit_driver(driver: WebDriver) -> None:
    driver.quit()
