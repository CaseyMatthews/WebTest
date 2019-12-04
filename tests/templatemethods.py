import unittest


class TemplateMethods(unittest.TestCase):

    def __init__(self, driver):

        super().__init__()

        self.driver = driver

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
