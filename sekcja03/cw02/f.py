import re


def test_jakania(tekst):
    """
    Funkcja sprawdza, czy ktoś się "jąka".

    :param tekst: testowany tekst
    :return: True - jeśli ktoś się "jąka", w przeciwnym razie - False

    Zakładamy, że jeśli w tekście występują co najmniej 2 identyczne litery obok siebie, to ktoś się "jąka"
    """
    regex = r'[a-z]*([a-z])\1[a-z]*'
    wzorzec = re.compile(regex)
    return wzorzec.search(tekst) is not None


if __name__ == '__main__':

    # przykładowe dane testowe
    dane_testowe = [
        'Mississippi',
        'kakao',
        'abrakadabra',
        'Halloween',
        'immunologia'
    ]

    print('CZY TEKST...        POWTARZA LITERY?')
    print('-' * 40)
    for testowany_tekst in dane_testowe:
        wynik_testu = test_jakania(testowany_tekst)
        print(f"{'\'' + testowany_tekst + '\'':20}{'TAK' if wynik_testu else 'NIE'}")
