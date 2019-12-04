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

    def dropdown_link(self, nav_item, dropdown_item, display_text, url):

        # The navigation dropdown link is not displayed by default.
        self.assertFalse(dropdown_item.is_displayed())

        # Hover over the navigation menu item.
        self.driver.hover_over(nav_item)

        # The navigation dropdown link is now displayed.
        self.assertTrue(dropdown_item.is_displayed())

        self.assertEqual(dropdown_item.text, display_text)

        # Click the navigation dropdown link.
        dropdown_item.click()

        # The appropriate python.org associated web page is navigated to.
        self.assertEqual(url, self.driver.current_url)

    def link(self, link, display_text, url):

        # The link is displayed by default.
        self.assertTrue(link.is_displayed())

        # The link displays the appropriate text.
        self.assertEqual(link.text, display_text)

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

    # TODO: Add logic to allow text read of the span elements contained inside the social links.

    def test_social_media_link_facebook(self):

        self.dropdown_link(self.header.social_drop_down,
                           self.header.facebook_link,
                           'Facebook',
                           'https://www.facebook.com/pythonlang?fref=ts')

    def test_social_media_link_twitter(self):

        self.dropdown_link(self.header.social_drop_down,
                           self.header.twitter_link,
                           'Twitter',
                           'https://twitter.com/ThePSF')

    def test_social_media_link_irc(self):

        self.dropdown_link(self.header.social_drop_down,
                           self.header.irc_link,
                           'Chat on IRC',
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
                  'PSF',
                  'https://www.python.org/psf-landing/')

    def test_sister_site_link_docs(self):

        self.link(self.header.sister_site_docs,
                  'Docs',
                  'https://docs.python.org/3/')

    def test_sister_site_link_pypi(self):

        self.link(self.header.sister_site_pypi,
                  'PyPI',
                  'https://pypi.org/')

    def test_sister_site_link_jobs(self):

        self.link(self.header.sister_site_jobs,
                  'Jobs',
                  'https://www.python.org/jobs/')

    def test_sister_site_link_community(self):

        self.link(self.header.sister_site_shop,
                  'Community',
                  'https://www.python.org/community/')

    def test_sister_site_link_python(self):

        self.header.sister_site_shop.click()

        self.header.sister_site_python.click()

        self.assertEqual('https://www.python.org/', self.driver.current_url)

    def test_about_apps(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_apps,
                           'Applications',
                           'https://www.python.org/about/apps/')

    def test_about_quotes(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_quotes,
                           'Quotes',
                           'https://www.python.org/about/quotes/')

    def test_about_getting_started(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_getting_started,
                           'Getting Started',
                           'https://www.python.org/about/gettingstarted/')

    def test_about_help(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_help,
                           'Help',
                           'https://www.python.org/about/help/')

    def test_about_python_brochure(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_py_brochure,
                           'Python Brochure',
                           'https://brochure.getpython.info/')

    def test_about_learn_more(self):

        self.dropdown_link(self.header.nav_about,
                           self.header.nav_about_learn_more,
                           'Learn more about Python.',
                           'https://www.python.org/about/')

    def test_downloads_all_releases(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_all_releases,
                           'All releases',
                           'https://www.python.org/downloads/')

    def test_downloads_source_code(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_source_code,
                           'Source code',
                           'https://www.python.org/downloads/source/')

    def test_downloads_windows(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_windows,
                           'Windows',
                           'https://www.python.org/downloads/windows/')

    def test_downloads_mac(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_mac,
                           'Mac OS X',
                           'https://www.python.org/downloads/mac-osx/')

    def test_downloads_other_platforms(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_other_platforms,
                           'Other Platforms',
                           'https://www.python.org/download/other/')

    def test_downloads_license(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_license,
                           'License',
                           'https://docs.python.org/3/license.html')

    def test_downloads_alternative_implementation(self):

        self.dropdown_link(self.header.nav_downloads,
                           self.header.nav_downloads_alt_imps,
                           'Alternative Implementations',
                           'https://www.python.org/download/alternatives/')

    def test_documentation_docs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_docs,
                           'Docs',
                           'https://www.python.org/doc/')

    def test_documentation_audio_visual_talks(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_audio_visual,
                           'Audio/Visual Talks',
                           'https://www.python.org/doc/av/')

    def test_documentation_beginners_guide(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_beginners_guide,
                           'Beginner\'s Guide',
                           'https://wiki.python.org/moin/BeginnersGuide')

    def test_documentation_devs_guide(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_devs_guide,
                           'Developer\'s Guide',
                           'https://devguide.python.org/')

    def test_documentation_faqs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_faq,
                           'FAQ',
                           'https://docs.python.org/3/faq/')

    def test_documentation_non_english_docs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_non_english_docs,
                           'Non-English Docs',
                           'https://wiki.python.org/moin/Languages')

    def test_documentation_pep_index(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_pep_index,
                           'PEP Index',
                           'https://www.python.org/dev/peps/')

    def test_documentation_python_books(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_py_books,
                           'Python Books',
                           'https://wiki.python.org/moin/PythonBooks')

    def test_documentation_python_essays(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_py_essays,
                           'Python Essays',
                           'https://www.python.org/doc/essays/')

    def test_documentation_python_3x_docs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_py3_docs,
                           'Python 3.x Docs',
                           'https://docs.python.org/3/')

    def test_documentation_python_2x_docs(self):

        self.dropdown_link(self.header.nav_documentation,
                           self.header.nav_documentation_py2_docs,
                           'Python 2.x Docs',
                           'https://docs.python.org/2/')

    def test_community_community_survey(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_survey,
                           'Community Survey',
                           'https://www.python.org/community/survey/')

    def test_community_diversity(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_diversity,
                           'Diversity',
                           'https://www.python.org/community/diversity/')

    def test_community_mailing_lists(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_mailing_lists,
                           'Mailing Lists',
                           'https://www.python.org/community/lists/')

    def test_community_irc(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_irc,
                           'IRC',
                           'https://www.python.org/community/irc/')

    def test_community_forums(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_forums,
                           'Forums',
                           'https://www.python.org/community/forums/')

    def test_community_pas_annual_impact_report(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_annual_impact_report,
                           'PSF Annual Impact Report',
                           'https://www.python.org/psf/annual-report/2019/')

    def test_community_python_conferences(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_py_conferences,
                           'Python Conferences',
                           'https://www.python.org/community/workshops/')

    def test_community_special_interest_groups(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_spec_interest_groups,
                           'Special Interest Groups',
                           'https://www.python.org/community/sigs/')

    def test_community_python_logo(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_py_logo,
                           'Python Logo',
                           'https://www.python.org/community/logos/')

    def test_community_python_wiki(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_py_wiki,
                           'Python Wiki',
                           'https://wiki.python.org/moin/')

    def test_community_merchandise(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_merchandise,
                           'Merchandise',
                           'https://www.python.org/community/merchandise/')

    def test_community_community_awards(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_awards,
                           'Community Awards',
                           'https://www.python.org/community/awards/')

    def test_community_code_of_conduct(self):

        self.dropdown_link(self.header.nav_community,
                           self.header.nav_comm_code_of_conduct,
                           'Code of Conduct',
                           'https://www.python.org/psf/conduct/')

    def test_success_stories_arts(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_arts,
                           'Arts',
                           'https://www.python.org/success-stories/category/arts/')

    def test_success_stories_business(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_business,
                           'Business',
                           'https://www.python.org/success-stories/category/business/')

    def test_success_stories_education(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_education,
                           'Education',
                           'https://www.python.org/success-stories/category/education/')

    def test_success_stories_engineering(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_engineering,
                           'Engineering',
                           'https://www.python.org/success-stories/category/engineering/')

    def test_success_stories_government(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_government,
                           'Government',
                           'https://www.python.org/success-stories/category/government/')

    def test_success_stories_scientific(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_scientific,
                           'Scientific',
                           'https://www.python.org/success-stories/category/scientific/')

    def test_success_stories_software_development(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_sw_dev,
                           'Software Development',
                           'https://www.python.org/success-stories/category/software-development/')

    def test_success_stories_Microsoft(self):

        self.dropdown_link(self.header.nav_success_stories,
                           self.header.nav_success_stories_microsoft,
                           'Microsoft',
                           'https://azure.microsoft.com/en-us/develop/python/')

    def test_news_python_news(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_py_news,
                           'Python News',
                           'https://www.python.org/blogs/')

    def test_news_psf_newsletter(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_psf_newsletter,
                           'PSF Newsletter',
                           'https://www.python.org/psf/newsletter/')

    def test_news_community_news(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_community_news,
                           'Community News',
                           'https://planetpython.org/')

    def test_news_psf_news(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_psf_news,
                           'PSF News',
                           'http://pyfound.blogspot.com/')

    def test_news_pycon_news(self):

        self.dropdown_link(self.header.nav_news,
                           self.header.nav_news_pycon_news,
                           'PyCon News',
                           'https://pycon.blogspot.com/')

    def test_events_python_events(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_py_events,
                           'Python Events',
                           'https://www.python.org/events/python-events')

    def test_events_user_group_events(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_user_group_events,
                           'User Group Events',
                           'https://www.python.org/events/python-user-group/')

    def test_events_python_events_archive(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_py_events_archive,
                           'Python Events Archive',
                           'https://www.python.org/events/python-events/past/')

    def test_events_user_group_events_archive(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_user_group_events_archive,
                           'User Group Events Archive',
                           'https://www.python.org/events/python-user-group/past/')

    def test_events_submit_an_event(self):

        self.dropdown_link(self.header.nav_events,
                           self.header.nav_events_submit_event,
                           'Submit an Event',
                           'https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event')


if __name__ == '__main__':

    unittest.main()
