import re


def test_czy_prawidlowy_numer(numer_telefonu):
    """
    Funkcja testuje, czy podany numer jest poprawnym, polskim numerem telefonu.
.
    :param numer_telefonu: testowany numer telefonu (podany jako tekst)
    :return: True - jeśli numer jest poprawny, w przeciwnym razie - False

    Za prawidłowy uważamy numer o postaci +48xxxxxxxxx, gdzie x - oznacza cyfrę
    """
    regex = r'^\+48\d{9}$'
    wzorzec = re.compile(regex)
    return wzorzec.search(numer_telefonu) is not None


if __name__ == '__main__':

    # przykładowe dane testowe
    testowe_numery_telefonow = [
        '+481234567890',
        '+48123456789',
        '+14812345678',
        ' +48123456789'
    ]

    print('CZY NUMER TELEFONU...      JEST POPRAWNY?')
    print('-' * 44)
    for nr_telefonu in testowe_numery_telefonow:
        wynik = test_czy_prawidlowy_numer(nr_telefonu)
        print(f"{'\'' + nr_telefonu + '\'':27}{'TAK' if wynik else 'NIE'}")
