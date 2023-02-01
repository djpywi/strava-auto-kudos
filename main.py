from KudosBot import StravaKudos
from selenium import webdriver


class SeleniumCrowd(StravaKudos):
    def __init__(self):
        super().__init__()
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Remote(command_executor=self.SERVER,
                                       options=self.options)
        self.driver.maximize_window()


crowd = SeleniumCrowd()
crowd.applause()