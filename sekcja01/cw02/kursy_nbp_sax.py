import xml.sax.handler as sh
from utils.kursy_nbp_utils import *
from xml.sax import make_parser
from urllib.request import urlopen


class HandlerKursowWalut(sh.ContentHandler):
    """
    Klasa handlera SAX dla kursów walut NBP.
    """

    def __init__(self):
        super().__init__()
        # atrybuty zawierające wyniki parsowania
        self.tabela_kursow = None
        self.nazwa_tabeli = None
        self.numer_tabeli = None
        self.data_tabeli = None

        # atrybuty pomocnicze
        self.waluta = None
        self.stos_elementow = []

    def startElement(self, name, attrs):
        self.stos_elementow.append(name)
        match name:
            case 'Rates':
                self.tabela_kursow = []
            case 'Rate':
                self.waluta = {}

    def characters(self, content):
        match self.stos_elementow[-1]:
            case 'Table':
                self.nazwa_tabeli = content
            case 'No':
                self.numer_tabeli = content
            case 'EffectiveDate':
                self.data_tabeli = content
            case 'Currency':
                self.waluta['currency'] = content
            case 'Code':
                self.waluta['code'] = content
            case 'Mid':
                self.waluta['mid'] = content

    def endElement(self, name):
        ostatni_otwarty_element = self.stos_elementow.pop()
        if ostatni_otwarty_element != name:
            raise Exception('Błąd parsowania...')
        if name == 'Rate':
            self.tabela_kursow.append(self.waluta)
            self.waluta = None


def parsuj_tabele_kursow():
    url = 'https://api.nbp.pl/api/exchangerates/tables/A?format=xml'
    odpowiedz = urlopen(url)

    handler = HandlerKursowWalut()
    parser = make_parser()
    parser.setContentHandler(handler)
    parser.parse(odpowiedz)
    return handler.numer_tabeli, handler.data_tabeli, handler.tabela_kursow


if __name__ == '__main__':
    numer_tabeli, data_tabeli, tabela_kursow = parsuj_tabele_kursow()
    tytul_tabeli = utworz_tytul_tabeli(numer_tabeli, data_tabeli)
    wypisz_tabele_kursow(tytul_tabeli, tabela_kursow)
