from xml.sax.handler import ContentHandler


class ProductsHandler(ContentHandler):

    def __init__(self):
        super().__init__()
        self.current_element_name = None
        self.products = []
        self.product = None
        self.contents = ''
        self.in_product = False

    def startElement(self, name, attributes):
        self.current_element_name = name
        if name == 'product':
            self.in_product = True
            self.product = {}
            for attr_name in attributes.getNames():
                self.product[attr_name] = attributes.getValue(attr_name)

    def characters(self, data):
        data = data.strip()
        if data:
            self.contents = data

    def endElement(self, name):
        if name == 'product':
            self.products.append(self.product)
            self.product = None
            self.in_product = False
        else:
            if self.in_product:
                self.product[self.current_element_name] = self.contents
            self.contents = ''
            self.current_element_name = None


if __name__ == '__main__':
    from xml.sax import make_parser
    from pprint import pprint

    parser = make_parser()
    handler = ProductsHandler()
    parser.setContentHandler(handler)
    parser.parse("../data/products.xml")

    pprint(handler.products)
