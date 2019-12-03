import unittest
from landingpagesubheader import LandingPageSubHeader
from webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import \
    ElementNotInteractableException

from time import sleep


class LandingPageSubHeaderTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()

        cls.driver.implicitly_wait(5)

        cls.subhdr = LandingPageSubHeader(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setUp(self):
        self.driver.get('http://www.python.org')

    def tearDown(self):
        pass

    def test_launch_shell_button(self):

        self.subhdr.launch_shell.click()


if __name__ == '__main__':

    unittest.main()
