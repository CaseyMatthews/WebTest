from header import Header
from elementmetadata import ElementMetaData


class LandingPageSubHeader(Header):

    def __init__(self, driver: object):

        super().__init__(driver)

        self.launch_shell = ElementMetaData(id='start-shell')

        self.link_1 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[1]/a')

        self.link_2 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[2]/a')

        self.link_3 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[3]/a')

        self.link_4 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[4]/a')

        self.link_5 = ElementMetaData(xpath='//*[@id="dive-into-python"]/ol/li[5]/a')

        self.console = ElementMetaData(xpath='//*[@id="dive-into-python"]/iframe')

        self.functions_in_python = ElementMetaData(xpath='//*[@id="dive-into-python"]/ul[2]/li[1]/div[2]/p/a')

        self.lists_in_python = ElementMetaData(xpath='//*[@id="dive-into-python"]/ul[2]/li[2]/div[2]/p/a')

        self.math_funcs_in_python = ElementMetaData(xpath='//*[@id="dive-into-python"]/ul[2]/li[3]/div[2]/p/a')

        self.whet_your_appetite = ElementMetaData(xpath='//*[@id="dive-into-python"]/ul[2]/li[4]/div[2]/p/a')

        self.control_flow_tools = ElementMetaData(xpath='//*[@id="dive-into-python"]/ul[2]/li[5]/div[2]/p/a')

        self.learn_more = ElementMetaData(xpath='//*[@id="touchnav-wrapper"]/header/div/div[3]/p/a')
