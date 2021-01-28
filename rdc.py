# Selenium imports
from selenium_scraper import Scraper
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Other imports
import os
import time


def rdc():
    email = input("Enter your email adress:")
    password = input("Enter your password:")
    beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
    url = "https://www.rueducommerce.fr/produit/be-quiet-new-product-20190123141548-71248041"
    browser = Scraper(headless=False).open_browser()
    browser.get(url)
    time.sleep(2)
    ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    browser.find_element_by_id("header-top__account").click()
    browser.find_element_by_id("login").send_keys(email)
    browser.find_element_by_id("login_pass").send_keys(password)
    browser.find_element_by_xpath("/html/body/div[2]/section/div/div/div[2]/div[1]/div/form/div/button").click()
    browser.get(url)
    # Set browser size to the minimum
    # browser.set_window_size(1, 1)
    # Move browser to the to right corner
    # browser.set_window_position(3390, 9*95)
    while True:
        try:
            browser.find_element_by_id("rgpd-allok").click()
            browser.find_element_by_id("add-product").click()
            time.sleep(1)
            browser.find_element_by_class_name("btn--prin").click()
            time.sleep(2)
            ActionChains(browser).send_keys(Keys.ESCAPE).perform()
            browser.find_element_by_id("rgpd-allok").click()
            order = browser.find_element_by_id("to-order")
            order.click()
            livraison = browser.find_elements_by_class_name("table__delivery-btn")
            livraison[2].find_element_by_tag_name("div").click()
            browser.maximize_window()
            beep(11000)
        except:
            time.sleep(6)
            browser.refresh()

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    rdc()