import unittest
from headernewnew import Header
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.header = Header('http://www.python.org', webdriver.Chrome)

    @classmethod
    def tearDownClass(cls):

        cls.header.close()

    def setUp(self):

        self.header.get('http://www.python.org')

    def tearDown(self):

        # self.header.close()
        pass

    def test_page_loaded(self):

        self.assertIn('Python', self.header.driver.title)

    def test_header_search_field_enter(self):

        self.header.send_keys(self.header.search_field, 'pycon' + Keys.ENTER)

        self.assertIn('Search Python.org', self.header.driver.page_source)

        self.assertIn('pycon', self.header.driver.page_source)

    def test_header_search_button(self):

        self.header.click(self.header.search_submit)

        self.assertIn('Search Python.org', self.header.driver.page_source)

    def test_social_media_link_facebook(self):

        self.header.hover_over(self.header.social_drop_down)

        self.header.click(self.header.facebook_link)

        self.assertIn('facebook', self.header.driver.page_source)

    def test_social_media_link_twitter(self):

        self.header.hover_over(self.header.social_drop_down)

        self.header.click(self.header.twitter_link)

        self.assertIn('twitter', self.header.driver.page_source)

    def test_social_media_link_irc(self):

        self.header.hover_over(self.header.social_drop_down)

        self.header.click(self.header.irc_link)

        self.assertIn('Internet Relay Chat', self.header.driver.page_source)

    def test_social_links_no_hover_not_clickable(self):

        self.assertRaises(ElementNotInteractableException, self.header.click, self.header.facebook_link)

        self.assertRaises(ElementNotInteractableException, self.header.click, self.header.twitter_link)

        self.assertRaises(ElementNotInteractableException, self.header.click, self.header.irc_link)

    def test_social_links_no_hover_not_displayed(self):

        self.assertFalse(self.header._get_element(self.header.twitter_link).is_displayed())

        self.assertFalse(self.header._get_element(self.header.facebook_link).is_displayed())

        self.assertFalse(self.header._get_element(self.header.irc_link).is_displayed())

    def test_social_links_display_on_hover(self):

        self.assertFalse(self.header._get_element(self.header.twitter_link).is_displayed())

        self.assertFalse(self.header._get_element(self.header.facebook_link).is_displayed())

        self.assertFalse(self.header._get_element(self.header.irc_link).is_displayed())

        self.header.hover_over(self.header.social_drop_down)

        self.assertTrue(self.header._get_element(self.header.twitter_link).is_displayed())

        self.assertTrue(self.header._get_element(self.header.facebook_link).is_displayed())

        self.assertTrue(self.header._get_element(self.header.irc_link).is_displayed())


    def test_sister_site_link_psf(self):
        pass

    def test_sister_site_link_docs(self):
        pass

    def test_sister_site_link_pypi(self):
        pass

    def test_sister_site_link_jobs(self):
        pass

    def test_sister_site_link_community(self):
        pass

    def test_sister_site_link_python(self):
        pass


if __name__ == '__main__':
    unittest.main()
