from KudosBot import StravaKudos
from decouple import config
from selenium import webdriver

# Login every 3-4 hours and hits the Button
KEEP_GOING = config("KEEP_GOING", default=True, cast=bool)


class Selenium_config(StravaKudos):
    def __init__(self):
        self.SERVER = config("SERVER")
        self.LOGIN = config("LOGIN")
        self.PASSWORD = config("PASSWORD")
        self.URL = config("URL")

        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(command_executor=self.SERVER,
                                       options=self.options)
        self.driver.maximize_window()


kudos = Selenium_config()

if KEEP_GOING:
    while KEEP_GOING:
        kudos.dothework()
        kudos.deep_sleep()
else:
    kudos.dothework()
