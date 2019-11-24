

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

    def print(self):

        print("               ID: ", self.id)
        print("             Name: ", self.name)
        print("            XPath: ", self.xpath)
        print("        Link Text: ", self.link_text)
        print("Partial Link Text: ", self.partial_link_text)
        print("         Tag Name: ", self.tag_name)
        print("       Class Name: ", self.class_name)
        print("     CSS Selector: ", self.css_selector)

    def _get_element(self):

        if item.id:
            return self.driver.find_element(by='id', value=item.id)
        elif item.xpath:
            return self.driver.find_element(by='xpath', value=item.xpath)
        elif item.link_text:
            return self.driver.find_element(by='link text', value=item.link_text)
        elif item.partial_link_text:
            return self.driver.find_element(by='partial link text',
                                            value=item.partial_link_text)
        elif item.name:
            return self.driver.find.element(by='name', value=item.name)
        elif item.tag_name:
            return self.driver.find_element(by='tag name', value=item.tag_name)
        elif item.class_name:
            return self.driver.find_element(by='class name', value=item.class_name)
        elif item.css_selector:
            return self.driver.find_element(by='css selector', value=item.css_selector)
        else:
            raise NoSuchElementException


if __name__ == "__main__":

    element = ElementMetaData(class_name='psf-meta', id='q')

    element.print()
