from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    REGION = (By.ID, "region")
    ROLE = (By.ID, "role")
    QUESTION = (By.ID, "q")
    ASK = (By.ID, "ask")
    ANSWER = (By.ID, "answer")
    CITES = (By.ID, "cites")
    DOCUMENT_PANEL = (
        By.CSS_SELECTOR,
        "aside.card.panel"
    )

    def __init__(self, driver):
        self.driver = driver

    def select_region(self, region):
        Select(
            self.driver.find_element(*self.REGION)
        ).select_by_visible_text(region)

    def select_role(self, role):
        Select(
            self.driver.find_element(*self.ROLE)
        ).select_by_visible_text(role)

    def enter_question(self, question):
        q = self.driver.find_element(*self.QUESTION)
        q.clear()
        q.send_keys(question)

    def click_ask(self):
        self.driver.find_element(
            *self.ASK
        ).click()

    def ask_question(self, question):
        self.enter_question(question)
        self.click_ask()

    def get_answer(self):
        return self.driver.find_element(
            *self.ANSWER
        ).text

    def get_citations(self):
        return self.driver.find_element(
            *self.CITES
        ).text

    def wait_for_answer(self):
        wait = WebDriverWait(
            self.driver,
            20
        )

        wait.until(
            lambda driver:
            driver.find_element(
                *self.ANSWER
            ).text.strip() != "Thinking..."
        )

        return self.driver.find_element(
            *self.ANSWER
        ).text

    def wait_for_citations(self):
        wait = WebDriverWait(
            self.driver,
            20
        )

        wait.until(
            lambda driver:
            driver.find_element(
                *self.CITES
            ).text.strip() != ""
        )

        return self.driver.find_element(
            *self.CITES
        ).text