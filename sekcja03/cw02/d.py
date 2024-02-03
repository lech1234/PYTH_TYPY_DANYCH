import re


def test_czy_prawidlowy_email(email):
    """
    Funkcja sprawdza, czy podany tekst jest prostym, prawidłowym adresem e-mail.

    :param email: testowany adres e-mail
    :return: True - jeśli adres jest poprawny, w przeciwnym razie - False

    W naszym przykładzie poprawny adres składa się z:
    - co najmniej 3 liter lub cyfr na początku
    - symbolu @
    - przynajmniej 1 litery lub cyfry
    - kropki
    - końcówki domeny: com, gov lub pl
    """
    regex = r'^\w{3,}@\w+\.(?:com|pl|gov)$'  # non-capturing group
    wzorzec = re.compile(regex)
    return wzorzec.search(email) is not None


if __name__ == '__main__':

    # przykładowe dane testowe
    adresy_testowe = [
        'zarzad@firma.com',
        'kontakt@cdv.pl',
        'szkolenia@altkom.pl',
        'abc@10minutemail.net',
        '@defxghi',
        'president@whitehouse.gov'
    ]

    print('CZY ADRES E-MAIL...        JEST POPRAWNY?')
    print('-' * 44)
    for adres_email in adresy_testowe:
        wynik_testu = test_czy_prawidlowy_email(adres_email)
        print(f"{'\'' + adres_email + '\'':27}{'TAK' if wynik_testu else 'NIE'}")
