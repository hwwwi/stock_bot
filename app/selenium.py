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

    def move_page(self, url):
        """
        Move browser page
        It will wait for 5 second to move
        """
        self.browser.get(url)
        for i in range(10):
            if self.browser.current_url == url:
                return True
            else:
                time.sleep(0.5)
        return False

    def wait_element_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            return element
        except TimeoutException:
            return None

    def is_selling(self, url):
        """ Check if product is selling """

        logging.info(f'Check URL: {url}')

        # Move page
        if not self.move_page(url):
            return False

        # Check product in stock
        buy_btn = self.wait_element_by_xpath(
            "//div[@class='btn_order' | @class='btn_order v2']/span[@class='buy']")
        if buy_btn:
            return buy_btn.find_element_by_xpath(".//a").get_attribute('class') != "_stopDefault"
        else:
            return False
