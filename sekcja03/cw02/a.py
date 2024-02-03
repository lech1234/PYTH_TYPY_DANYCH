import re


def test_czy_tak_sie_konczy(tekst, sufiks):
    """
    Funkcja testuje, czy podany tekst kończy się podanym przyrostkiem.
.
    :param tekst: testowany tekst
    :param sufiks: końcówka tekstu
    :return: True - jeśli tekst kończy się podanym przyrostkiem, w przeciwnym razie - False
    """
    regex = f'{sufiks}$'
    wzorzec = re.compile(regex)
    return wzorzec.search(tekst) is not None


if __name__ == '__main__':

    # przykładowe dane testowe
    dane_testowe = [
        # (tekst, koncowka)
        ('abcfoo', 'foo'),
        ('fooabc', 'foo'),
        ('abcfooabc', 'foo'),
        (' foo ', 'foo')
    ]

    print('CZY TEKST...      KOŃCZY SIĘ NA...')
    print('-' * 44)
    for slowo, koncowka in dane_testowe:
        wynik = test_czy_tak_sie_konczy(slowo, koncowka)
        print(f"{'\'' + slowo + '\'':18}{'\'' + koncowka + '\'':20}{'TAK' if wynik else 'NIE'}")
