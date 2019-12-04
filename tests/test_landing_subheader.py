import unittest
from landingpagesubheader import LandingPageSubHeader
from webdriver import WebDriver
from tests.templatemethods import TemplateMethods as tmp


class LandingPageSubHeaderTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver()

        cls.driver.implicitly_wait(10)

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

        self.driver.switch_to.frame(self.subhdr.console)

        self.assertIn('>>>', self.driver.page_source)


if __name__ == '__main__':

    unittest.main()
