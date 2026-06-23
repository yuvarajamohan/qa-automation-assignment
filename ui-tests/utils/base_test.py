import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )

        self.driver.maximize_window()

        self.driver.get(
            "https://main-knowledge-assistant.newpage.workers.dev"
        )

    def tearDown(self):
        print("\nWaiting 5 seconds before closing browser...")
        time.sleep(5)
        self.driver.quit()