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

        # TODO: The link has the appropriate text.

        # Click the navigation dropdown link.
        dropdown_item.click()

        # The appropriate python.org associated web page is navigated to.
        self.assertEqual(url, self.driver.current_url)

    def link(self, link, url):

        # The link is displayed by default.
        self.assertTrue(link.is_displayed())

        # TODO: The link displays the appropriate text.

        # Click the link.
        link.click()

        # The appropriate page is navigated to.
        self.assertEqual(url, self.driver.current_url)

    #########
    # Tests #
    #########

    def test_page_loaded(self):

        self.assertIn('Python', self.driver.title)

    def test_header_search_field(self):

        self.header.search_field.send_keys('pycon' + Keys.ENTER)

        self.assertIn('Search Python.org', self.driver.page_source)

        self.assertIn('pycon', self.driver.page_source)

    def test_header_search_button(self):

        self.header.search_submit.click()

        self.assertIn('Search Python.org', self.driver.page_source)

    def test_social_media_link_facebook(self):

        self.dropdown_link(self.header.social_drop_down,
                           self.header.facebook_link,
                           'https://www.facebook.com/pythonlang?fref=ts')

    def test_social_media_link_twitter(self):

        self.dropdown_link(self.header.social_drop_down,
                           self.header.twitter_link,
                           'https://twitter.com/ThePSF')

    def test_social_media_link_irc(self):

        self.dropdown_link(self.header.social_drop_down,
                           self.header.irc_link,
                           'https://www.python.org/community/irc/')

    def test_social_links_no_hover_not_clickable(self):

        self.assertRaises(ElementNotInteractableException,
                          self.driver.click, self.header.facebook_link)

        self.assertRaises(ElementNotInteractableException,
                          self.driver.click, self.header.twitter_link)

        self.assertRaises(ElementNotInteractableException,
                          self.driver.click, self.header.irc_link)

    def test_sister_site_link_psf(self):

        self.link(self.header.sister_site_psf,
                  'https://www.python.org/psf-landing/')

    def test_sister_site_link_docs(self):

        self.link(self.header.sister_site_docs,
                  'https://docs.python.org/3/')

    def test_sister_site_link_pypi(self):

        self.link(self.header.sister_site_pypi,
                  'https://pypi.org/')

    def test_sister_site_link_jobs(self):

        self.link(self.header.sister_site_jobs,
                  'https://www.python.org/jobs/')

    def test_sister_site_link_community(self):

        self.link(self.header.sister_site_shop,
                  'https://www.python.org/community/')

    def test_sister_site_link_python(self):

        self.header.sister_site_shop.click()

        self.header.sister_site_python.click()

        self.assertEqual('https://www.python.org/', self.driver.current_url)

    def test_about_apps(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_apps,
                           'https://www.python.org/about/apps/')

    def test_about_quotes(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_quotes,
                           'https://www.python.org/about/quotes/')

    def test_about_getting_started(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_getting_started,
                           'https://www.python.org/about/gettingstarted/')

    def test_about_help(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_help,
                           'https://www.python.org/about/help/')

    def test_about_python_brochure(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_py_brochure,
                           'https://brochure.getpython.info/')

    def test_about_learn_more(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_learn_more,
                           'https://www.python.org/about/')

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
                           'https://docs.python.org/3/license.html')

    def test_downloads_alternative_implementation(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_alt_imps,
                           'https://www.python.org/download/alternatives/')

    def test_documentation_docs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_docs,
                           'https://www.python.org/doc/')

    def test_documentation_audio_visual_talks(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_audio_visual,
                           'https://www.python.org/doc/av/')

    def test_documentation_beginners_guide(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_beginners_guide,
                           'https://wiki.python.org/moin/BeginnersGuide')

    def test_documentation_devs_guide(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_devs_guide,
                           'https://devguide.python.org/')

    def test_documentation_faqs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_faq,
                           'https://docs.python.org/3/faq/')

    def test_documentation_non_english_docs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_non_english_docs,
                           'https://wiki.python.org/moin/Languages')

    def test_documentation_pep_index(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_pep_index,
                           'https://www.python.org/dev/peps/')

    def test_documentation_python_books(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_py_books,
                           'https://wiki.python.org/moin/PythonBooks')

    def test_documentation_python_essays(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_py_essays,
                           'https://www.python.org/doc/essays/')

    def test_documentation_python_3x_docs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_py3_docs,
                           'https://docs.python.org/3/')

    def test_documentation_python_2x_docs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_py2_docs,
                           'https://docs.python.org/2/')

    def test_community_community_survey(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_survey,
                           'https://www.python.org/community/survey/')

    def test_community_diversity(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_diversity,
                           'https://www.python.org/community/diversity/')

    def test_community_mailing_lists(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_mailing_lists,
                           'https://www.python.org/community/lists/')

    def test_community_irc(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_irc,
                           'https://www.python.org/community/irc/')

    def test_community_forums(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_forums,
                           'https://www.python.org/community/forums/')

    def test_community_pas_annual_impact_report(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_annual_impact_report,
                           'https://www.python.org/psf/annual-report/2019/')

    def test_community_python_conferences(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_py_conferences,
                           'https://www.python.org/community/workshops/')

    def test_community_special_interest_groups(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_spec_interest_groups,
                           'https://www.python.org/community/sigs/')

    def test_community_python_logo(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_py_logo,
                           'https://www.python.org/community/logos/')

    def test_community_python_wiki(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_py_wiki,
                           'https://wiki.python.org/moin/')

    def test_community_merchandise(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_merchandise,
                           'https://www.python.org/community/merchandise/')

    def test_community_community_awards(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_awards,
                           'https://www.python.org/community/awards/')

    def test_community_code_of_conduct(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_code_of_conduct,
                           'https://www.python.org/psf/conduct/')

    def test_success_stories_arts(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_arts,
                           'https://www.python.org/success-stories/category/arts/')

    def test_success_stories_business(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_business,
                           'https://www.python.org/success-stories/category/business/')

    def test_success_stories_education(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_education,
                           'https://www.python.org/success-stories/category/education/')

    def test_success_stories_engineering(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_engineering,
                           'https://www.python.org/success-stories/category/engineering/')

    def test_success_stories_government(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_government,
                           'https://www.python.org/success-stories/category/government/')

    def test_success_stories_scientific(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_scientific,
                           'https://www.python.org/success-stories/category/scientific/')

    def test_success_stories_software_development(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_sw_dev,
                           'https://www.python.org/success-stories/category/software-development/')

    def test_success_stories_Microsoft(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_microsoft,
                           'https://azure.microsoft.com/en-us/develop/python/')

    def test_news_python_events(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_py_news,
                           'https://www.python.org/blogs/')

    def test_news_psf_newsletter(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_psf_newsletter,
                           'https://www.python.org/psf/newsletter/')

    def test_news_community_news(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_community_news,
                           'https://planetpython.org/')

    def test_news_psf_news(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_psf_news,
                           'http://pyfound.blogspot.com/')

    def test_news_pycon_news(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_pycon_news,
                           'https://pycon.blogspot.com/')

    def test_events_python_events(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_py_events,
                           'https://www.python.org/events/python-events')

    def test_events_user_group_events(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_user_group_events,
                           'https://www.python.org/events/python-user-group/')

    def test_events_python_events_archive(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_py_events_archive,
                           'https://www.python.org/events/python-events/past/')

    def test_events_user_group_events_archive(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_user_group_events_archive,
                           'https://www.python.org/events/python-user-group/past/')

    def test_events_submit_an_event(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_submit_event,
                           'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event')


if __name__ == '__main__':

    unittest.main()
