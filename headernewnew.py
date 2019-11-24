from page import Page
from selenium import webdriver
from elementmetadata import ElementMetaData


class Header(Page):

    def __init__(self, url, driver):

        super().__init__(url, driver)

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

        self.facebook_link = ElementMetaData(class_name='icon-facebook')

        self.twitter_link = ElementMetaData(class_name='icon-twitter')

        self.irc_link = ElementMetaData(class_name='icon-freenode')


if __name__ == "__main__":

    hdr = Header('http://www.python.org', webdriver.Chrome)

    hdr.hover_over(hdr.social_drop_down)

    hdr.click(hdr.twitter_link)
