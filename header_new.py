import basepage
from selenium import webdriver


class Header(basepage.BasePage):

    def __init__(self, url, driver):

        super().__init__(url, driver)

        self.elements = {

            'sister-site-python': 'python-meta',

            'sister-site-psf': 'psf-meta',

            'sister-site-docs': 'docs-meta',

            'sister-site-pypi': 'pypi-meta',

            'sister-site-jobs': 'jobs-meta',

            'sister-site-shop': 'shop-meta',

            # Miscellaneous header elements

            'site-logo': 'python-logo',

            'donate-button': 'donate-button',

            }

    # Action methods.

    def click_element(self, element):

        self._get_element_by_class_name(element).click()

    def _get_element_by_class_name(self, class_name):

        return self.driver.find_element_by_class_name(class_name)


if __name__ == "__main__":

    h = Header('http://www.python.org', webdriver.Chrome)

    h.click_element(h.elements['sister-site-docs'])
