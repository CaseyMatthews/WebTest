import unittest
from header import Header
from webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import \
    ElementNotInteractableException


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = WebDriver()

        cls.driver.implicitly_wait(5)

        cls.header = Header(cls.driver)

    @classmethod
    def tearDownClass(cls):

        cls.driver.close()

    def setUp(self):

        self.driver.get('http://www.python.org')

    def tearDown(self):

        pass

    #########################
    # Test Template Methods #
    #########################

    def dropdown_link(self, nav_item, dropdown_item, url):

        # The navigation dropdown link is not displayed by default.
        self.assertFalse(dropdown_item.is_displayed())

        # Hover over the navigation menu item.
        self.driver.hover_over(nav_item)

        # The navigation dropdown link is now displayed.
        self.assertTrue(dropdown_item.is_displayed())

        # Click the navigation dropdown link.
        dropdown_item.click()

        # The appropriate python.org associated web page is navigated to.
        self.assertTrue(url, self.driver.current_url)

    #########
    # Tests #
    #########

    def test_page_loaded(self):

        self.assertIn('Python', self.driver.title)

    def test_header_search_field_enter(self):

        self.header.search_field.send_keys('pycon' + Keys.ENTER)

        self.assertIn('Search Python.org', self.driver.page_source)

        self.assertIn('pycon', self.driver.page_source)

    def test_header_search_button(self):

        self.header.search_submit.click()

        self.assertIn('Search Python.org', self.driver.page_source)

    def test_social_media_link_facebook(self):

        self.driver.hover_over(self.header.social_drop_down)

        self.header.facebook_link.click()

        self.assertIn('facebook', self.driver.page_source)

    def test_social_media_link_twitter(self):

        self.driver.hover_over(self.header.social_drop_down)

        self.header.twitter_link.click()

        self.assertIn('twitter', self.driver.page_source)

    def test_social_media_link_irc(self):

        self.driver.hover_over(self.header.social_drop_down)

        self.header.irc_link.click()

        self.assertIn('Internet Relay Chat', self.driver.page_source)

    def test_social_links_no_hover_not_clickable(self):

        self.assertRaises(ElementNotInteractableException,
                          self.driver.click, self.header.facebook_link)

        self.assertRaises(ElementNotInteractableException,
                          self.driver.click, self.header.twitter_link)

        self.assertRaises(ElementNotInteractableException,
                          self.driver.click, self.header.irc_link)

    def test_social_twitter_link_not_displayed(self):

        self.assertFalse(self.header.twitter_link.is_displayed())

    def test_social_facebook_link_not_displayed(self):

        self.assertFalse(self.header.facebook_link.is_displayed())

    def test_social_irc_link_not_displayed(self):

        # self.assertFalse(self.header._get_element(self.header.irc_link).is_displayed())

        self.assertFalse(self.header.irc_link.is_displayed())

    def test_social_twitter_display_on_hover(self):

        self.driver.hover_over(self.header.social_drop_down)

        self.assertTrue(self.header.twitter_link.is_displayed())

    def test_social_facebook_display_on_hover(self):

        self.driver.hover_over(self.header.social_drop_down)

        self.assertTrue(self.header.facebook_link.is_displayed())

    def test_social_irc_display_on_hover(self):

        self.driver.hover_over(self.header.social_drop_down)

        self.assertTrue(self.header.irc_link.is_displayed())

    def test_sister_site_link_psf(self):

        self.header.sister_site_psf.click()

        self.assertEqual('https://www.python.org/psf-landing/', self.driver.current_url)

    def test_sister_site_link_docs(self):

        self.header.sister_site_docs.click()

        self.assertEqual('https://docs.python.org/3/', self.driver.current_url)

    def test_sister_site_link_pypi(self):

        self.header.sister_site_pypi.click()

        self.assertEqual('https://pypi.org/', self.driver.current_url)

    def test_sister_site_link_jobs(self):

        self.header.sister_site_jobs.click()

        self.assertEqual('https://www.python.org/jobs/', self.driver.current_url)

    def test_sister_site_link_community(self):

        self.header.sister_site_shop.click()

        self.assertEqual('https://www.python.org/community/', self.driver.current_url)

    def test_sister_site_link_python(self):

        self.header.sister_site_shop.click()

        self.header.sister_site_python.click()

        self.assertEqual('https://www.python.org/', self.driver.current_url)

    def test_about_applications_link_not_displayed(self):

        self.assertFalse(self.header.nav_about_apps.is_displayed())

    def test_about_quotes_link_not_displayed(self):

        self.assertFalse(self.header.nav_about_quotes.is_displayed())

    def test_about_getting_started_link_not_displayed(self):

        self.assertFalse(
            self.header.nav_about_getting_started.is_displayed())

    def test_about_help_link_not_displayed(self):

        self.assertFalse(self.header.nav_about_help.is_displayed())

    def test_about_python_brochure_link_not_displayed(self):

        self.assertFalse(self.header.nav_about_py_brochure.is_displayed())

    def test_about_learn_more_link_not_displayed(self):

        self.assertFalse(self.header.nav_about_learn_more.is_displayed())

    def test_about_applications_display_on_hover(self):

        self.driver.hover_over(self.header.nav_about)

        self.assertTrue(self.header.nav_about_apps.is_displayed())

    def test_about_quotes_display_on_hover(self):

        self.driver.hover_over(self.header.nav_about)

        self.assertTrue(self.header.nav_about_quotes.is_displayed())

    def test_about_getting_started_display_on_hover(self):

        self.driver.hover_over(self.header.nav_about)

        self.assertTrue(
            self.header.nav_about_getting_started.is_displayed())

    def test_about_help_display_on_hover(self):

        self.driver.hover_over(self.header.nav_about)

        self.assertTrue(self.header.nav_about_help.is_displayed())

    def test_about_python_brochure_display_on_hover(self):

        self.driver.hover_over(self.header.nav_about)

        self.assertTrue(self.header.nav_about_py_brochure.is_displayed())

    def test_about_learn_more_display_on_hover(self):

        self.driver.hover_over(self.header.nav_about)

        self.assertTrue(self.header.nav_about_learn_more.is_displayed())

    def test_about_apps_click(self):

        self.driver.hover_over(self.header.nav_about)

        self.header.nav_about_apps.click()

        self.assertEqual('https://www.python.org/about/apps/', self.driver.current_url)

    def test_about_quotes_click(self):

        self.driver.hover_over(self.header.nav_about)

        self.header.nav_about_quotes.click()

        self.assertEqual('https://www.python.org/about/quotes/', self.driver.current_url)

    def test_about_getting_started_click(self):

        self.driver.hover_over(self.header.nav_about)

        self.header.nav_about_getting_started.click()

        self.assertEqual('https://www.python.org/about/gettingstarted/', self.driver.current_url)

    def test_about_help_click(self):

        self.driver.hover_over(self.header.nav_about)

        self.header.nav_about_py_brochure.click()

        self.assertEqual('https://brochure.getpython.info/', self.driver.current_url)

    def test_downloads_all_releases_not_displayed(self):

        self.assertFalse(self.header.nav_downloads_all_releases.is_displayed())

    def test_downloads_source_code_not_displayed(self):

        self.assertFalse(self.header.nav_downloads_source_code.is_displayed())

    def test_downloads_windows_not_displayed(self):

        self.assertFalse(self.header.nav_downloads_dwnld_windows.is_displayed())

    def test_downloads_mac_not_displayed(self):

        self.assertFalse(self.header.nav_downloads_mac.is_displayed())

    def test_downloads_other_platforms_not_displayed(self):

        self.assertFalse(self.header.nav_downloads_other_platforms.is_displayed())

    def test_downloads_license_not_displayed(self):

        self.assertFalse(self.header.nav_downloads_license.is_displayed())

    def test_downloads_alternative_implementation_not_displayed(self):

        self.assertFalse(self.header.nav_downloads_alt_imps.is_displayed())

    def test_downloads_download_windows_not_displayed(self):

        self.assertFalse(self.header.nav_downloads_dwnld_windows.is_displayed())

    def test_downloads_all_releases(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_all_releases,
                           'https://www.python.org/downloads/')

    def test_downloads_source_code(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_source_code,
                           'https://www.python.org/downloads/source/')

    def test_downloads_windows(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_windows,
                           'https://www.python.org/downloads/windows/')

    def test_downloads_mac(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_mac,
                           'https://www.python.org/downloads/mac-osx/')

    def test_downloads_other_platforms(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_other_platforms,
                           'https://www.python.org/download/other/')

    def test_downloads_license(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_license,
                           'https://www.python.org/download/other/')

    def test_downloads_alternative_implementation(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_alt_imps,
                           'https://www.python.org/download/alternatives/')

    def test_documentation_docs_not_displayed(self):

        self.assertFalse(self.header.nav_documentation_docs.is_displayed())


if __name__ == '__main__':

    unittest.main()
