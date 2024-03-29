from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException


class Page:

    def __init__(self, url, driver):
        """
        This class represents a basic web page. It defines attributes and methods
        that will be shared by all web pages.
        :param url: A URL for the desired starting web page.
        :param driver: A selenium web driver (IE, Firefox, Chrome).
        """

        self.url = url  # Address of web page to open.

        self.driver = driver()  # Selenium web driver instance.

        self.driver.get(url)  # Open the web page in the browser.

        self.driver.implicitly_wait(10)  # Driver actions time out after 10 seconds.

    ########################
    # Public action methods.
    ########################

    def close(self):

        self.driver.close()

    def get(self, url):

        self.driver.get(url)

    def click(self, element):

        element = self._get_element(element)

        if element.is_displayed():

            element.click()

        else:

            raise ElementNotInteractableException

    def hover_over(self, element):

        element = self._get_element(element)

        hover = ActionChains(self.driver).move_to_element(element)

        hover.perform()

    def send_keys(self, element, key_sequence):

        element = self._get_element(element)

        element.send_keys(key_sequence)

    #########################
    # Private helper methods.
    #########################

    def _get_element(self, element):

        if element.id:
            return self.driver.find_element(by='id', value=element.id)
        elif element.xpath:
            return self.driver.find_element(by='xpath', value=element.xpath)
        elif element.link_text:
            return self.driver.find_element(by='link text', value=element.link_text)
        elif element.partial_link_text:
            return self.driver.find_element(by='partial link text',
                                            value=element.partial_link_text)
        elif element.name:
            return self.driver.find.element(by='name', value=element.name)
        elif element.tag_name:
            return self.driver.find_element(by='tag name', value=element.tag_name)
        elif element.class_name:
            return self.driver.find_element(by='class name', value=element.class_name)
        elif element.css_selector:
            return self.driver.find_element(by='css selector', value=element.css_selector)
        else:

            pass
