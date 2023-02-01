import random
import time
from decouple import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

KEEP_GOING = config("KEEP_GOING")

class StravaKudos:

    def __init__(self):
        self.SERVER = config("SERVER")
        self.LOGIN = config("LOGIN")
        self.PASSWORD = config("PASSWORD")
        self.URL = config("URL")
        self.KEEP_GOING = KEEP_GOING

    def take_nap(self):
        nap_time = random.randint(3, 7)
        time.sleep(nap_time)

    def deep_sleep(self):
        interval = random.randint(10800, 14400)
        time.sleep(interval)

    # Navigate to Strava and fills out credentials
    def load_page(self):
        self.driver.get(self.URL)
        self.take_nap()
        username = self.driver.find_element(By.NAME, "email")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(self.LOGIN)
        password.send_keys(self.PASSWORD)
        self.take_nap()
        password.send_keys(Keys.RETURN)

    def thumbs_up(self):
        # Click buttons with "Give Kudos" title
        self.take_nap()
        self.driver.execute_script(
            "document.querySelectorAll('[title=\"Give kudos\"]').forEach(button => button.click());")
        self.take_nap()

        # Click buttons with "Be the first to give kudos!" title
        self.driver.execute_script(
            "document.querySelectorAll('[title=\"Be the first to give kudos!\"]').forEach(button => button.click());")
        self.take_nap()
        self.driver.close()

    def dothework(self):
        self.load_page()
        self.thumbs_up()

    def give_kudos(self):
        if self.KEEP_GOING:
            while self.KEEP_GOING:
                self.dothework()
                self.deep_sleep()
        else:
            self.dothework()
