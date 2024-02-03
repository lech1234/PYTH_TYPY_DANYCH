"""
Użycie modułu getopt do przekazywania argumentów i opcji z zewnątrz.

Moduł należy uruchomić z okna terminala, np.:

python info_getopt.py Pomocy!
python info_getopt.py -p 3 Pomocy!
python info_getopt.py -p 3 -d Pomocy!
python info_getopt.py --liczba_powtorzen 3 --duze_litery Pomocy!

Uwaga: kolejność podawania danych nie ma znaczenia (zwyczajowo najpierw opcje, potem argumenty)
"""
import getopt
import sys


def info(komunikat, liczba_powtorzen, duze_litery):
    print('\nARGUMENTY WEWNĄTRZ FUNKCJI info:')
    print(f'\tkomunikat:        {komunikat}')
    print(f'\tliczba_powtorzen: {liczba_powtorzen}')
    print(f'\tduze_litery:      {duze_litery}')
    print('\nWYNIK WYWOŁANIA:')
    liczba_powtorzen = int(liczba_powtorzen)
    komunikaty = [komunikat] * liczba_powtorzen
    if duze_litery:
        komunikaty = map(str.upper, komunikaty)
    print(*komunikaty, sep='\n')


def odbierz_parametry_z_wiersza_polecen():
    argumenty_wiersza_polecen = sys.argv[1:]
    krotkie_nazwy_opcji = 'p:d'
    dlugie_nazwy_opcji = ['liczba_powtorzen=', 'duze_litery']
    lista_opcji, lista_argumentow = getopt.getopt(argumenty_wiersza_polecen, krotkie_nazwy_opcji, dlugie_nazwy_opcji)
    # wartości domyślne:
    liczba_powtorzen = 1
    duze_litery = False

    for opcja, wartosc in lista_opcji:
        if opcja in ('-p', '--liczba_powtorzen'):
            liczba_powtorzen = int(wartosc)
        elif opcja in ('-d', '--duze_litery'):
            duze_litery = True

    # 1 argument jest obowiązkowy!
    if len(lista_argumentow) == 1:
        komunikat = lista_argumentow[0]
    else:
        raise SyntaxError('usage: info_getopt [-p LICZBA_POWTORZEN] [-d DUZE_LITERY] komunikat')
    return komunikat, liczba_powtorzen, duze_litery


if __name__ == '__main__':
    argumenty = odbierz_parametry_z_wiersza_polecen()
    info(*argumenty)
