

class BasePage:

    def __init__(self, url, driver):
        """
        This class represents a basic web page. It defines attributes and methods
        that will be shared by all web pages.
        :param driver: A selenium web driver (IE, Firefox, Chrome).
        """

        self.url = url

        self.driver = driver()

        self.driver.get(url)

        self.driver.implicitly_wait(10)
