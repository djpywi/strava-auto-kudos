from KudosBot import StravaKudos
from decouple import config
from selenium import webdriver

# Login every 3-4 hours and hits the Button
KEEP_GOING = config("KEEP_GOING", default=True, cast=bool)


class SeleniumConfig(StravaKudos):
    def __init__(self):
        super().__init__()
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(command_executor=self.SERVER,
                                       options=self.options)
        self.driver.maximize_window()


assisant = SeleniumConfig()
assisant.give_kudos()