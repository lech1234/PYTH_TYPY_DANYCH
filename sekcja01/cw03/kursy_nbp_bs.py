import bs4 as bs
import urllib.request as req
from utils.kursy_nbp_utils import *


def pobierz_nazwe_tabeli(dokument):
    """
    Funkcja wyszukuje w dokumencie element <h1>.

    :param dokument: dokument sparsowany
    :return: tytuł dokumentu zapisany dużymi literami

    Zakładamy, że ten element <h1> zawiera tytuł dokumentu.
    """
    # print(dokument)
    element_h1 = dokument.find('h1')
    return element_h1.string.upper()


def pobierz_dane_tabeli(element_table):
    """

    :param element_table: element <table> w sparsowanym dokumencie
    :return: lista wierszy z danymi tabela (każdy wiersz jest listą)

    Zakładamy, że tabela ma następującą strukturę:
    <table>
      ...
      <tbody>
        <tr>
          <td>dana 1 w wierszu 1</td>
          ...
        </tr>
        ...
      </tbody>
    </table>
    """
    element_tbody = element_table.tbody
    lista_list = [[element_td.string for element_td in element_tr.find_all('td')]
                  for element_tr in element_tbody.find_all('tr')]
    klucze = 'currency', 'code', 'mid'
    return map(lambda dane_lista: dict(zip(klucze, dane_lista)), lista_list)


def parsuj_tabele_kursow():
    url = 'https://nbp.pl/statystyka-i-sprawozdawczosc/kursy/tabela-a/'
    # odpowiedz = req.urlopen(url)

    # jeśli nie działa można zastąpić linijkę wyżej, następująco:
    odpowiedz = req.urlopen(req.Request(url, headers={
        'Host': 'nbp.pl',
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64;rv: 120.0) Gecko/20100101 Firefox/120.0',
        'Accept-Encoding': 'UTF-8',
        'Accept': 'text/html'
    }))

    dokument_html = odpowiedz.read()
    # parsowanie dokumentu HTML
    dokument_bs = bs.BeautifulSoup(dokument_html, 'html.parser')

    # jeśli trzeba kod HTML załadować z lokalnego pliku...
    # with open('kursy_nbp.html', mode='rt', encoding='utf-8') as plik:
    #     dokument_bs = bs.BeautifulSoup(plik, 'html.parser')

    tabela_bs = dokument_bs.find('table')
    # print(element_table.prettify())

    tytul = pobierz_nazwe_tabeli(dokument_bs)
    dane = pobierz_dane_tabeli(tabela_bs)
    return tytul, dane


if __name__ == '__main__':
    tytul_tabeli, dane_tabeli = parsuj_tabele_kursow()
    wypisz_tabele_kursow(tytul_tabeli, dane_tabeli)
