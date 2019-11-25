from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class WebDriver(webdriver.Chrome):

    def __init__(self):

        super().__init__()

    def hover_over(self, element):

        hover = ActionChains(self).move_to_element(element)

        hover.perform()

    @staticmethod
    def click(element):

        element.click()


if __name__ == "__main__":

    driver = WebDriver()
