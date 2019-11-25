from selenium.common.exceptions import NoSuchElementException
from elementmetadata import ElementMetaData


class PageObject:

    def __init__(self, webdriver):

        self.driver = webdriver

    # TODO: Refactor to rely on 'item' interface rather than type.
    def __getattribute__(self, item):

        item = object.__getattribute__(self, item)

        if isinstance(item, ElementMetaData):

            item = object.__getattribute__(self, '_get_element')(item)

        return item

    # TODO: Implement error handling and selector priority.
    def _get_element(self, element):

        if element.id:

            return self.driver.find_element(by='id', value=element.id)

        elif element.xpath:

            return self.driver.find_element(by='xpath', value=element.xpath)

        elif element.link_text:

            return self.driver.find_element(by='link text', value=element.link_text)

        elif element.partial_link_text:

            return self.driver.find_element(by='partial link text',
                                            value=element.partial_link_text)

        elif element.name:

            return self.driver.find.element(by='name', value=element.name)

        elif element.tag_name:

            return self.driver.find_element(by='tag name', value=element.tag_name)

        elif element.class_name:

            return self.driver.find_element(by='class name', value=element.class_name)

        elif element.css_selector:

            return self.driver.find_element(by='css selector', value=element.css_selector)

        else:

            raise NoSuchElementException


