from KudosBot import StravaKudos
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class LocalCrowd(StravaKudos):
    def __init__(self):
        super().__init__()
        self.options = Options()
        # self.options.add_experimental_option("detach", True) # keeps the selenium controlled browser open
        # self.options.add_argument("--headless") # headless mode for server commandline usage
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.chrome_prefs = {}
        self.options.experimental_options["prefs"] = self.chrome_prefs
        self.chrome_prefs["profile.default_content_settings"] = {"images": 2}  # disables images
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.URL)


crowd = LocalCrowd()
crowd.applause()
