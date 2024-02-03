import xml.sax.handler as sh


class SaxHandler(sh.ContentHandler):

    def startDocument(self):
        print('[początek dokumentu]')

    def endDocument(self):
        print('[koniec dokumentu]')

    def startElement(self, name, attrs):
        print(f'[znacznik otwierający]: element=\'{name}\', atrybuty={attrs.items()}')

    def endElement(self, name):
        print(f'[znacznik domykający] : element=\'{name}\'')

    def characters(self, content):
        print(f'[zawartość znakowa]   : {content!r}')


if __name__ == '__main__':
    from xml.sax import make_parser

    parser = make_parser()
    handler = SaxHandler()
    parser.setContentHandler(handler)
    parser.parse('towary.xml')
