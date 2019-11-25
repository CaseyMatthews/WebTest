from depreciated.page import Page
from selenium import webdriver
from elementmetadata import ElementMetaData


class Header(Page):

    def __init__(self, url, driver):

        super().__init__(url, driver)

        # TODO: Look into converting dictionary to class member variables.
        self.elements = {

            # Sister site links.

            'sister-site-python': ElementMetaData(class_name='python-meta'),

            'sister-site-psf': ElementMetaData(class_name='psf-meta'),

            'sister-site-docs': ElementMetaData(class_name='docs-meta'),

            'sister-site-pypi': ElementMetaData(class_name='pypi-meta'),

            'sister-site-jobs': ElementMetaData(class_name='jobs-meta'),

            'sister-site-shop': ElementMetaData(class_name='shop-meta'),

            # Miscellaneous header elements.

            'site-logo': ElementMetaData(class_name='python-logo'),

            'donate-button': ElementMetaData(class_name='donate-button'),

            # Search bar elements.

            'search-field': ElementMetaData(class_name='search-field'),

            'search-submit': ElementMetaData(class_name='search-button'),

            # Social media links.

            'social-drop-down': ElementMetaData(class_name='winkwink-nudgenudge'),

            'facebook-link': ElementMetaData(class_name='icon-facebook'),

            'twitter-link': ElementMetaData(class_name='icon-twitter'),

            'irc-link': ElementMetaData(class_name='icon-freenode')

            }  # End header elements.


if __name__ == "__main__":

    hdr = Header('http://www.python.org', webdriver.Chrome)

    hdr.hover_over(hdr.elements['social-drop-down'])

    hdr.click(hdr.elements['twitter-link'])
