"""
Użycie listy sys.argv do przekazywania argumentów i opcji z zewnątrz.

Moduł należy uruchomić z okna terminala, np.:

python info_argv.py Pomocy!
python info_argv.py Pomocy! 3
python info_argv.py Pomocy! 3 True

Uwaga: kolejność podawania danych jest istotna!
"""
import sys


def info(komunikat, liczba_powtorzen, duze_litery):
    print('\nARGUMENTY WEWNĄTRZ FUNKCJI info:')
    print(f'\tkomunikat:        {komunikat}')
    print(f'\tliczba_powtorzen: {liczba_powtorzen}')
    print(f'\tduze_litery:      {duze_litery}')
    print('\nWYNIK WYWOŁANIA:')
    komunikaty = [komunikat] * liczba_powtorzen
    if duze_litery:
        komunikaty = map(str.upper, komunikaty)
    print(*komunikaty, sep='\n')


def odbierz_parametry_z_wiersza_polecen():
    match len(sys.argv):
        case 2:
            param_komunikat, param_liczba_powtorzen, param_duze_litery = sys.argv[1], 1, False
        case 3:
            param_komunikat, param_liczba_powtorzen, param_duze_litery = sys.argv[1], sys.argv[2], False
        case 4:
            param_komunikat, param_liczba_powtorzen, param_duze_litery = sys.argv[1:]
        case _:
            raise SyntaxError('usage: info_argv KOMUNIKAT [LICZBA_POWTORZEN] [DUZE_LITERY]')
    param_liczba_powtorzen = int(param_liczba_powtorzen)
    param_duze_litery = bool(param_duze_litery)
    return param_komunikat, param_liczba_powtorzen, param_duze_litery


if __name__ == '__main__':
    argumenty = odbierz_parametry_z_wiersza_polecen()
    info(*argumenty)
