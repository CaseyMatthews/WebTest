

class Locators:
    """ """

    def __init__(self, id=None, name=None, xpath=None, link_text=None,
                 partial_link_text=None, tag_name=None, class_name=None,
                 css_selector=None):

        self.id = id

        self.name = name

        self.xpath = xpath

        self.link_text = link_text

        self.partial_link_text = partial_link_text

        self.tag_name = tag_name

        self.class_name = class_name

        self.css_selector = css_selector
