from pageobject import PageObject
from elementmetadata import ElementMetaData
from webdriver import WebDriver


class Header(PageObject):

    def __init__(self, driver: object):

        super().__init__(driver)

        ####################
        # Sister site links.
        ####################

        self.sister_site_python = ElementMetaData(class_name='python-meta')

        self.sister_site_psf = ElementMetaData(class_name='psf-meta')

        self.sister_site_docs = ElementMetaData(class_name='docs-meta')

        self.sister_site_pypi = ElementMetaData(class_name='pypi-meta')

        self.sister_site_jobs = ElementMetaData(class_name='jobs-meta')

        self.sister_site_shop = ElementMetaData(class_name='shop-meta')

        ################################
        # Miscellaneous header elements.
        ################################

        self.site_logo = ElementMetaData(class_name='python-logo')

        self.donate_button = ElementMetaData(class_name='donate-button')

        ######################
        # Search bar elements.
        ######################

        self.search_field = ElementMetaData(class_name='search-field')

        self.search_submit = ElementMetaData(class_name='search-button')

        #####################
        # Social media links.
        #####################

        self.social_drop_down = ElementMetaData(class_name='winkwink-nudgenudge')

        self.facebook_link = ElementMetaData(
            xpath='//*[@id="touchnav-wrapper"]/header/div/div[1]/div/div[2]/ul/li/ul/li[1]/a')

        self.twitter_link = ElementMetaData(
            xpath='//*[@id="touchnav-wrapper"]/header/div/div[1]/div/div[2]/ul/li/ul/li[2]/a')

        self.irc_link = ElementMetaData(
            xpath='//*[@id="touchnav-wrapper"]/header/div/div[1]/div/div[2]/ul/li/ul/li[3]/a')

        ##########################
        # Navigation bar elements.
        ##########################

        self.nav_about = ElementMetaData(id='about')

        self.nav_downloads = ElementMetaData(id='downloads')

        self.nav_documentation = ElementMetaData(id='documentation')

        self.nav_community = ElementMetaData(id='community')

        self.nav_success_stories = ElementMetaData(id='success-stories')

        self.nav_news = ElementMetaData(id='news')

        self.nav_events = ElementMetaData(id='events')

        ##############################
        # Navigation bar sub-elements.
        ##############################

        # About sub-menu elements.

        self.nav_about_apps = ElementMetaData(xpath='//*[@id="about"]/ul/li[1]/a')

        self.nav_about_quotes = ElementMetaData(xpath='//*[@id="about"]/ul/li[2]/a')

        self.nav_about_getting_started = ElementMetaData(xpath='//*[@id="about"]/ul/li[3]/a')

        self.nav_about_help = ElementMetaData(xpath='//*[@id="about"]/ul/li[4]/a')

        self.nav_about_py_brochure = ElementMetaData(xpath='//*[@id="about"]/ul/li[5]/a')

        self.nav_about_learn_more = ElementMetaData(xpath='//*[@id="about"]/ul/li[6]/p/a')

        # Downloads sub-menu elements.

        self.nav_downloads_all_releases = ElementMetaData(xpath='//*[@id="downloads"]/ul/li[1]/a')

        self.nav_downloads_source_code = ElementMetaData(xpath='//*[@id="downloads"]/ul/li[2]/a')

        self.nav_downloads_windows = ElementMetaData(xpath='//*[@id="downloads"]/ul/li[3]/a')

        self.nav_downloads_mac = ElementMetaData(xpath='//*[@id="downloads"]/ul/li[4]/a')

        self.nav_downloads_other_platforms = ElementMetaData(xpath='//*[@id="downloads"]/ul/li[5]/a')

        self.nav_downloads_license = ElementMetaData(xpath='//*[@id="downloads"]/ul/li[6]/a')

        self.nav_downloads_alt_imps = ElementMetaData(xpath='//*[@id="downloads"]/ul/li[7]/a')

        self.nav_downloads_dwnld_windows = ElementMetaData(xpath='//*[@id="downloads"]/ul/li[8]/div[3]/p[1]/a')

        # Documentation sub-menu elements.

        self.nav_documentation_docs = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[1]/a')

        self.nav_documentation_audio_visual = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[2]/a')

        self.nav_documentation_beginners_guide = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[3]/a')

        self.nav_documentation_devs_guide = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[4]/a')

        self.nav_documentation_faq = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[5]/a')

        self.nav_documentation_non_english_docs = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[6]/a')

        self.nav_documentation_pep_index = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[7]/a')

        self.nav_documentation_py_books = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[8]/a')

        self.nav_documentation_py_essays = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[9]/a')

        self.nav_documentation_py3_docs = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[10]/p[2]/a[1]')

        self.nav_documentation_py2_docs = ElementMetaData(xpath='//*[@id="documentation"]/ul/li[10]/p[2]/a[2]')

        # Community sub-menu elements.

        self.nav_comm_survey = ElementMetaData(xpath='//*[@id="community"]/ul/li[1]/a')

        self.nav_comm_diversity = ElementMetaData(xpath='//*[@id="community"]/ul/li[2]/a')

        self.nav_comm_mailing_lists = ElementMetaData(xpath='//*[@id="community"]/ul/li[3]/a')

        self.nav_comm_irc = ElementMetaData(xpath='//*[@id="community"]/ul/li[4]/a')

        self.nav_comm_forums = ElementMetaData(xpath='//*[@id="community"]/ul/li[5]/a')

        self.nav_comm_annual_impact_report = ElementMetaData(xpath='//*[@id="community"]/ul/li[6]/a')

        self.nav_comm_py_conferences = ElementMetaData(xpath='//*[@id="community"]/ul/li[7]/a')

        self.nav_comm_spec_interest_groups = ElementMetaData(xpath='//*[@id="community"]/ul/li[8]/a')

        self.nav_comm_py_logo = ElementMetaData(xpath='//*[@id="community"]/ul/li[9]/a')

        self.nav_comm_py_wiki = ElementMetaData(xpath='//*[@id="community"]/ul/li[10]/a')

        self.nav_comm_merchandise = ElementMetaData(xpath='//*[@id="community"]/ul/li[11]/a')

        self.nav_comm_awards = ElementMetaData(xpath='//*[@id="community"]/ul/li[12]/a')

        self.nav_comm_code_of_conduct = ElementMetaData(xpath='//*[@id="community"]/ul/li[13]/a')

        # Success stories sub-menu elements.

        self.nav_success_stories_arts = ElementMetaData(xpath='//*[@id="success-stories"]/ul/li[1]/a')

        self.nav_success_stories_business = ElementMetaData(xpath='//*[@id="success-stories"]/ul/li[2]/a')

        self.nav_success_stories_education = ElementMetaData(xpath='//*[@id="success-stories"]/ul/li[3]/a')

        self.nav_success_stories_engineering = ElementMetaData(xpath='//*[@id="success-stories"]/ul/li[4]/a')

        self.nav_success_stories_government = ElementMetaData(xpath='//*[@id="success-stories"]/ul/li[5]/a')

        self.nav_success_stories_scientific = ElementMetaData(xpath='//*[@id="success-stories"]/ul/li[6]/a')

        self.nav_success_stories_sw_dev = ElementMetaData(xpath='//*[@id="success-stories"]/ul/li[7]/a')

        self.nav_success_stories_microsoft = ElementMetaData(xpath='//*[@id="success-stories"]/ul/li[8]/p/a')

        # News sub-menu elements.

        self.nav_news_py_news = ElementMetaData(xpath='//*[@id="news"]/ul/li[1]/a')

        self.nav_news_psf_newsletter = ElementMetaData(xpath='//*[@id="news"]/ul/li[2]/a')

        self.nav_news_community_news = ElementMetaData(xpath='//*[@id="news"]/ul/li[3]/a')

        self.nav_news_psf_news = ElementMetaData(xpath='//*[@id="news"]/ul/li[4]/a')

        self.nav_news_pycon_news = ElementMetaData(xpath='//*[@id="news"]/ul/li[5]/a')

        # Events sub-menu elements.

        self.nav_events_py_events = ElementMetaData(xpath='//*[@id="events"]/ul/li[1]/a')

        self.nav_events_user_group_events = ElementMetaData(xpath='//*[@id="events"]/ul/li[2]/a')

        self.nav_events_py_events_archive = ElementMetaData(xpath='//*[@id="events"]/ul/li[3]/a')

        self.nav_events_user_group_events_archive = ElementMetaData(xpath='//*[@id="events"]/ul/li[4]/a')

        self.nav_events_submit_event = ElementMetaData(xpath='//*[@id="events"]/ul/li[5]/a')


if __name__ == "__main__":

    chrome = WebDriver()

    hdr = Header(chrome)

    chrome.get("http://www.python.org")

    hdr.sister_site_docs.click()

    chrome.back()

    hdr.sister_site_psf.click()

    chrome.back()

    chrome.hover_over(hdr.social_drop_down)

    chrome.hover_over(hdr.social_drop_down)

    hdr.twitter_link.click()
