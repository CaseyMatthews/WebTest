from header import Header
from selenium import webdriver
from time import sleep


class LandingPage(Header):

    def __init__(self, url, driver):

        super().__init__(url, driver)

    def click_top_bar_links(self):

        for _ in range(0, 60):

            sleep(1)

            if _ % 6 == 0:

                self.click_python_link()

            elif _ % 6 == 1:

                self.click_psf_link()

            elif _ % 6 == 2:

                self.click_docs_link()

            elif _ % 6 == 3:

                self.click_pypi_link()
                print("pypi")

            elif _ % 6 == 4:

                self.click_jobs_link()

            elif _ % 6 == 5:

                self.click_shop_link()


if __name__ == "__main__":

    lp = LandingPage('http://www.python.org', webdriver.Chrome)

    # lp.click_top_bar_links()

    lp.click_pypi_link()
