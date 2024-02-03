import re


def wybor_osoby(osoba):
    """
    Funkcja wyszukuje osoby o imieniu Jan i nazwisku kończącym się na -ski, ale nie Kowalskich.

    :param osoba: imię i nazwisko osoby
    :return: imię osoby (o ile jest nim Jan), w przeciwnym razie None

    Osoba jest opisana przez: Imię Nazwisko
    W rozwiązaniu wykorzystane są asercje lookahead
    """
    regex = r'(Jan)(?=\s[A-Z][a-z]+ski)(?!\sKowalski)'
    wzorzec = re.compile(regex)
    if dopasowanie := wzorzec.search(osoba):
        return dopasowanie.group()


if __name__ == '__main__':

    # przykładowe dane testowe
    osoby_testowe = [
        'Jan Sobieski',
        'Jan Kowalski',
        'Adam Nowakowski',
        'Jan Adamowicz',
        'Jan Kownacki',
        'Jan Dynowski',
        'Janusz Kowalski'
    ]

    print('OSOBA...                      WYBÓR')
    print('-' * 60)
    for osoba_testowa in osoby_testowe:
        wynik_wyboru = wybor_osoby(osoba_testowa)
        print(f"{osoba_testowa:30}{wynik_wyboru if wynik_wyboru else '-'}")
