import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config

SERVER = "10.10.1.38:4444"
LOGIN = "erwin@posteo.de"
PASSWORD = """2%FAV'?>'-"H11:Els{;!!J`Crz*jTKm"""
URL = "https://www.strava.com/dashboard/following/40"

class StravaKudos:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(command_executor=SERVER,
                                       options=self.options)
        self.driver.maximize_window()

    def load_page(self):
        self.driver.get(URL)
        time.sleep(3)
        username = self.driver.find_element(By.NAME, "email")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(LOGIN)
        password.send_keys(PASSWORD)
        time.sleep(3)
        password.send_keys(Keys.RETURN)

    def thumbs_up(self):
        while True:
            self.driver.execute_script("document.querySelectorAll('[title=\"Give kudos\"]').forEach(button => button.click());")
            refresher = random.randint(1800, 4800)
            time.sleep(refresher)
            self.driver.refresh()


kudos = StravaKudos()
kudos.load_page()
kudos.thumbs_up()
