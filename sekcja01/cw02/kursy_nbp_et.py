import urllib.request as req
import xml.etree.ElementTree as et
from utils.kursy_nbp_utils import *


def parsuj_tabele_kursow():
    url = 'https://api.nbp.pl/api/exchangerates/tables/A?format=xml'
    odpowiedz = req.urlopen(url)
    dane_xml = odpowiedz.read()
    drzewo_xml = et.fromstring(dane_xml)

    element_ExchangeRatesTable = drzewo_xml.find('ExchangeRatesTable')
    numer_tabeli = element_ExchangeRatesTable.find('No').text
    data_tabeli = element_ExchangeRatesTable.find('EffectiveDate').text

    tabela_kursow = []
    for element_Rate in element_ExchangeRatesTable.findall('Rates/Rate'):
        waluta = {
            'currency': element_Rate.find('Currency').text,
            'code': element_Rate.find('Code').text,
            'mid': element_Rate.find('Mid').text
        }
        tabela_kursow.append(waluta)
    return numer_tabeli, data_tabeli, tabela_kursow


if __name__ == '__main__':
    numer_tabeli, data_tabeli, tabela_kursow = parsuj_tabele_kursow()
    tytul_tabeli = utworz_tytul_tabeli(numer_tabeli, data_tabeli)
    wypisz_tabele_kursow(tytul_tabeli, tabela_kursow)
