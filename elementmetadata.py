

class ElementMetaData:
    """ """

    def __init__(self, *, id=None, name=None, xpath=None, link_text=None,
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

        # TODO: Implement more meta-data into this object (like link url) to minimize maintenance?

    def print(self):

        print("               ID: ", self.id)
        print("             Name: ", self.name)
        print("            XPath: ", self.xpath)
        print("        Link Text: ", self.link_text)
        print("Partial Link Text: ", self.partial_link_text)
        print("         Tag Name: ", self.tag_name)
        print("       Class Name: ", self.class_name)
        print("     CSS Selector: ", self.css_selector)


if __name__ == "__main__":

    element = ElementMetaData(class_name='psf-meta', id='q')

    element.print()
