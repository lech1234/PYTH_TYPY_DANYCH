import configparser as cp


def parsuj_ustawienia(plik_ustawien):
    ustawienia = cp.ConfigParser()
    ustawienia.read(plik_ustawien)
    return ustawienia


def info(ustawienia):
    nazwy_sekcji = ustawienia.sections()
    print('SEKCJE:', nazwy_sekcji)

    for nazwa_sekcji in nazwy_sekcji:
        sekcja = ustawienia[nazwa_sekcji]
        print(f'\n<SEKCJA {sekcja.name}>')

        for klucz, wartosc in sekcja.items():
            print(f'\t{klucz}: {wartosc}')


if __name__ == '__main__':
    konfiguracja = parsuj_ustawienia('db.ini')
    info(konfiguracja)
