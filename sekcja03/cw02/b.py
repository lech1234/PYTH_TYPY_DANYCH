import re


def test_czy_tak_sie_zaczyna(tekst, prefiks):
    """
    Funkcja testuje, czy podany tekst zaczyna się podanym przedrostekiem.
.
    :param tekst: testowany tekst
    :param prefiks: początek tekstu
    :return: True - jeśli tekst zaczyna się podanym przedrostkiem, w przeciwnym razie - False
    """
    regex = f'^{prefiks}'
    wzorzec = re.compile(regex)
    return wzorzec.search(tekst) is not None


if __name__ == '__main__':

    # przykładowe dane testowe
    dane_testowe = [
        # (tekst, początek)
        ('abcfoo', 'foo'),
        ('fooabc', 'foo'),
        ('abcfooabc', 'foo'),
        (' foo ', 'foo')
    ]

    print('CZY TEKST...      ZACZYNA SIĘ NA...')
    print('-' * 44)
    for slowo, przedrostek in dane_testowe:
        wynik = test_czy_tak_sie_zaczyna(slowo, przedrostek)
        print(f"{'\'' + slowo + '\'':18}{'\'' + przedrostek + '\'':20}{'TAK' if wynik else 'NIE'}")
