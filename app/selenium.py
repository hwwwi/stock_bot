import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException


class ChromeSelenium(object):
    def __init__(self):
        """ Init """

        self.browser = self.initialize_driver()

    def initialize_driver(self):
        """ Initialize selenium driver"""

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_driver = webdriver.Chrome(chrome_options=chrome_options)

        return chrome_driver

    def is_selling(self, url):
        """ Check if product is selling """

        logging.info(f'Check URL: {url}')
        # {self.browser.current_url}
