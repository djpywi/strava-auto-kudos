import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config


class StravaKudos:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(command_executor=config("SELENIUMSERVER"),
                                       options=self.options)
        self.driver.maximize_window()

    def load_page(self):
        self.driver.get(config("URL"))
        time.sleep(3)
        username = self.driver.find_element(By.NAME, "email")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(config("LOGIN"))
        password.send_keys(config("PASSWORD"))
        time.sleep(3)
        password.send_keys(Keys.RETURN)

    def thumbs_up(self):
        while True:
            self.driver.execute_script("document.querySelectorAll('[title=\"Give kudos\"]').forEach(button => button.click());")
            time.sleep(3600)
            self.driver.refresh()


kudos = StravaKudos()
kudos.load_page()
kudos.thumbs_up()
