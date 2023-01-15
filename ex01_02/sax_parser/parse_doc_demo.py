from xml.sax.handler import ContentHandler


class ProductsHandler(ContentHandler):
    def startDocument(self):
        print('[start document]')

    def endDocument(self):
        print('[end document]')

    def startElement(self, name, attrs):
        print(f'[start element]: name={name}, attrs={attrs.items()}')

    def endElement(self, name):
        print(f'[end element]: name={name}')

    def characters(self, content):
        print(f'[characters]: {repr(content)}')


if __name__ == '__main__':
    from xml.sax import make_parser

    parser = make_parser()
    handler = ProductsHandler()
    parser.setContentHandler(handler)
    parser.parse("../data/products.xml")
