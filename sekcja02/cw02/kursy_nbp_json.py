import json
import urllib.request as req
from utils.kursy_nbp_utils import *


def parsuj_tabele_kursow():
    url = 'https://api.nbp.pl/api/exchangerates/tables/A?format=json'
    odpowiedz = req.urlopen(url)
    dane_json = odpowiedz.read()

    dane = json.loads(dane_json.decode('utf-8'))[0]  # wynikiem jest element z 1-elementowej listy
    numer_tabeli = dane['no']
    data_tabeli = dane['effectiveDate']
    tabela_kursow = dane['rates']
    return numer_tabeli, data_tabeli, tabela_kursow


if __name__ == '__main__':
    numer_tabeli, data_tabeli, tabela_kursow = parsuj_tabele_kursow()
    tytul_tabeli = utworz_tytul_tabeli(numer_tabeli, data_tabeli)
    wypisz_tabele_kursow(tytul_tabeli, tabela_kursow)
