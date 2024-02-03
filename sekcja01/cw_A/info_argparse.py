"""
Użycie modułu argparse do przekazywania argumentów i opcji z zewnątrz.

Moduł należy uruchomić z okna terminala, np.:

python info_argparse.py --help
python info_argparse.py Pomocy!
python info_argparse.py -p 3 Pomocy!
python info_argparse.py -p 3 -d Pomocy!
python info_argparse.py --liczba_powtorzen 3 --duze_litery Pomocy!

Uwaga: kolejność podawania danych nie ma znaczenia (zwyczajowo najpierw opcje, potem argumenty)
"""
import argparse


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
    parser = argparse.ArgumentParser(
        prog='info_argparse',
        description='Program powtarza podany komunikat zadaną liczbę razy')

    # argument pozycyjny (obowiązkowy)
    parser.add_argument('komunikat')

    # opcja (wymaga podania wartości, domyślnie: 1)
    parser.add_argument('-p', '--liczba_powtorzen', type=int, default=1)

    # opcja (flaga, domyślnie: False)
    parser.add_argument('-d', '--duze_litery', action='store_true')

    args = parser.parse_args()
    return args.komunikat, args.liczba_powtorzen, args.duze_litery


if __name__ == '__main__':
    argumenty = odbierz_parametry_z_wiersza_polecen()
    info(*argumenty)
