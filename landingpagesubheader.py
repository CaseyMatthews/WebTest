from pageobject import PageObject
from elementmetadata import ElementMetaData
from webdriver import WebDriver


class LandingPageSubHeader(PageObject):

    def __init__(self, driver: object):

        super().__init__(driver)

        self.launch_shell = ElementMetaData(id='start-shell')

        self.link_1 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[1]/a')

        self.link_2 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[2]/a')

        self.link_3 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[3]/a')

        self.link_4 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[4]/a')

        self.link_5 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[5]/a')