import re


def test_czy_to_palindrom(tekst):
    """
    Funkcja sprawdza, czy podany tekst jest 4- lub 5-literowym palindromem (wielkość liter jest nieistotna).

    :param tekst: testowany tekst
    :return: True - jeśli to palindrom, w przeciwnym razie - False
    """
    regex = r'^([a-z])([a-z])[a-z]?\2\1$'
    wzorzec = re.compile(regex, flags=re.I)  # ignorujemy wielkość liter
    return wzorzec.search(tekst) is not None


if __name__ == '__main__':

    # przykładowe dane testowe
    dane_testowe = [
        'kajak',
        'mama',
        'radar',
        'Abba'
    ]

    print('CZY TEKST...        JEST PALINDROMEM?')
    print('-' * 40)
    for potencjalny_palindrom in dane_testowe:
        wynik_testu = test_czy_to_palindrom(potencjalny_palindrom)
        print(f"{'\'' + potencjalny_palindrom + '\'':20}{'TAK' if wynik_testu else 'NIE'}")
