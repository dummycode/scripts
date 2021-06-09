import threading
import pause
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Config
USERNAME = "henrythomasharris@gmail.com"
PASSWORD = "L*sZCgz3F1"
GO_TIME = datetime(2021, 6, 4, 15, 0, 0)
EVENT_URL = "https://www.recreation.gov/ticket/233338/ticket/16"

# Params
GUEST_COUNT = 10
DEBUG_DATE = "Saturday, July 24, 2021, available"
TEST_DATE = "Saturday, June 5, 2021, available"
REAL_DATE = "Saturday, June 12, 2021, available"
DEBUG_TIMES = ["0800", "0900"]
TEST_TIMES = ["0800", "0900", "0945"]
REAL_TIMES = ["0800", "0900", "0945", "1000", "1045", "1100", "1200", "1245", "1300", "1345", "1400", "1430", "1500", "1530"]


def wait_by_xpath(driver, xpath, wait=10):
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))


def login(driver):
    """
    Login to recreation.gov
    """
    print("Logging in...")

    login_link = driver.find_element_by_id("ga-global-nav-log-in-link")
    login_link.click()

    driver.find_element_by_id("rec-acct-sign-in-email-address").send_keys(USERNAME)
    driver.find_element_by_id("rec-acct-sign-in-password").send_keys(PASSWORD)

    driver.find_element_by_xpath('//*[@title="Log In"]').click()


def wait_till_time(time=GO_TIME):
    print("Waiting until go time...")
    pause.until(time)


def set_date(driver):
    print("Setting date...")

    wait_by_xpath(driver, '//*[@id="tourCalendarWithKey"]')
    driver.find_element_by_id("tourCalendarWithKey").click()

    if False:
        # TODO: Disable
        xpath = '//*[@aria-label="Move forward to switch to the next month."]'
        class_name = "rec-icon-arrow-forward"

        wait = WebDriverWait(driver, 10)
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, class_name)))

        driver.find_element_by_class_name("right").click()


    xpath = '//*[@aria-label="' + TEST_DATE + '"]'
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))

    driver.find_element_by_xpath(xpath).click()


def set_time(driver, time):
    print("Setting time...")

    wait = WebDriverWait(driver, 10)
    men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@data-component="RadioPill"]')))

    time = driver.find_element_by_xpath('//*[@value="' + time + '"]')
    time.find_element_by_xpath("..").click()


def set_count(driver):
    """
    Set guest count
    """
    print("Setting ticket count...")

    driver.find_element_by_id("guest-counter").click()

    for i in range(GUEST_COUNT - 1):
        driver.find_element_by_xpath('//*[@aria-label="Add General Admissions"]').click()

    close_xpath = '//*[@data-component="ContentBlock"]'
    wait_by_xpath(driver, close_xpath)
    driver.find_element_by_xpath(close_xpath).click()


def add_to_cart(driver):
    print("Adding to cart...")

    add_to_cart_xpath = '//*[text() = "Add to Cart"]'
    wait_by_xpath(driver, add_to_cart_xpath)
    span = driver.find_element_by_xpath(add_to_cart_xpath)

    span.find_element_by_xpath("../..").click()


def book_tickets(driver, time):
    print("Booking tickets for time " + time)

    driver.get(EVENT_URL)

    login(driver)

    wait_till_time()

    driver.get(EVENT_URL)

    print("GO GO GO! " + time)

    set_date(driver)
    set_time(driver, time)
    set_count(driver)
    add_to_cart(driver)


def main():
    print("Yerd")

    for time in TEST_TIMES:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome()

        thread = threading.Thread(target=book_tickets, args=(driver, time))
        thread.start()


if __name__ == "__main__":
    main()
    while True:
        pass
