from depreciated.page import Page
from selenium import webdriver


class Header(Page):

    def __init__(self, url, driver):

        super().__init__(url, driver)

    # Sister site links.

    def _get_psf_link(self):

        return self.driver.find_element_by_class_name('psf-meta')

    def _get_python_link(self):

        return self.driver.find_element_by_class_name('python-meta')

    def _get_docs_link(self):

        return self.driver.find_element_by_class_name('docs-meta')

    def _get_pypi_link(self):

        return self.driver.find_element_by_class_name('pypi-meta')

    def _get_jobs_link(self):

        return self.driver.find_element_by_class_name('jobs-meta')

    def _get_shop_link(self):

        return self.driver.find_element_by_class_name('shop-meta')

    # Miscellaneous header elements.

    def _get_python_logo_link(self):

        return self.driver.find_element_by_class_name('python-logo')

    def _get_donate_button_link(self):

        return self.driver.find_element_by_class_name('donate-button')

    # Search bar elements.

    def _get_search_field(self):

        return self.driver.find_element_by_class_name('search-field')

    def _get_search_submit_button(self):

        return self.driver.find_element_by_class_name('search-button')

    # Social media links.

    def _get_social_media_drop_down(self):

        return self.driver.find_element_by_class_name('winkwink-nudgenudge')

    def _get_facebook_link(self):

        return self.driver.find_element_by_class_name('icon-facebook')

    def _get_twitter_link(self):

        return self.driver.find_element_by_class_name('icon-twitter')

    def _get_irc_chat_link(self):

        return self.driver.find_element_by_class_name('icon-freenode')

    # Sister site link actions.

    def click_psf_link(self):

        self._get_psf_link().click()

    def click_python_link(self):

        self._get_python_link().click()

    def click_docs_link(self):

        self._get_docs_link().click()

    def click_pypi_link(self):

        self._get_pypi_link().click()

    def click_jobs_link(self):

        self._get_jobs_link().click()

    def click_shop_link(self):

        self._get_shop_link().click()


if __name__ == "__main__":

    h = Header('http://www.python.org', webdriver.Chrome)

