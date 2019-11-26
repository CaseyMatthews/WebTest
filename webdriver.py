from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class WebDriver(webdriver.Chrome):

    def __init__(self):

        super().__init__()

    def hover_over(self, element):

        hover = ActionChains(self).move_to_element(element)

        hover.perform()

    @staticmethod
    def click(element):

        element.click()

    def explicit_wait(self, element):

        WebDriverWait(self, 10).until(
            ec.visibility_of_element_located((By.XPATH, element)))


if __name__ == "__main__":

    driver = WebDriver()
