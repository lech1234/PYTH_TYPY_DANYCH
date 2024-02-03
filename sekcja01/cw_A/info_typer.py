"""
Użycie modułu typer do przekazywania argumentów i opcji z zewnątrz.

Moduł należy uruchomić z okna terminala, np.:

python info_typer.py --help
python info_typer.py Pomocy!
python info_typer.py --liczba-powtorzen 3 Pomocy!
python info_typer.py --liczba-powtorzen 3 --duze-litery Pomocy!

Uwaga: kolejność podawania danych nie ma znaczenia (zwyczajowo najpierw opcje, potem argumenty)
       w nazwach opcji występują myślniki, a nie podkreślenia!
"""
import typer
from typing_extensions import Annotated


def info(komunikat: Annotated[str, typer.Argument(help='komunikat do wyświetlenia')],
         liczba_powtorzen: Annotated[int, typer.Option('--liczba-powtorzen', '-p',
                                                       help='liczba powtórzeń komunikatu')] = 1,
         duze_litery: Annotated[bool, typer.Option('--duze-litery', '-d',
                                                   help='czy komunikat ma być wypisany dużymi literami')] = False):
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


if __name__ == '__main__':
    typer.run(info)
