from selenium.common.exceptions import NoSuchElementException

class PageObject:

    def __getattribute__(self, item):

        item = object.__getattribute__(self, item)


