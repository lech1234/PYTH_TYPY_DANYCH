import csv


def listy_do_csv(plik_csv, listy, naglowki):
    """
    Funkcja tworzy plik w formacie CSV na podstawie sekwencji list.

    :param plik_csv: nazwa i położenie pliku CSV
    :param listy: sekwencja list
    :param naglowki: tytuły nagłówków w pliku CSV
    :return: None
    """
    with open(plik_csv, mode='wt', encoding='utf-8', newline='') as plik:
        csv_writer = csv.writer(plik, delimiter=',')
        csv_writer.writerow(naglowki)
        for lista in listy:
            csv_writer.writerow(lista)


def csv_do_list(plik_csv):
    """
    Funkcja czyta dane z pliku CSV i zwraca w postaci sekwencji list

    :param plik_csv: nazwa i położenie pliku CSV
    :return: krotka zawierająca listę tytułów nagłówków oraz listy z danych (każdy wiersz to osobna lista)
    """
    with open(plik_csv, mode='rt', encoding='utf-8', newline='') as plik:
        csv_reader = csv.reader(plik, delimiter=',')
        naglowki, *listy_danych = list(csv_reader)
    return naglowki, listy_danych


if __name__ == '__main__':
    nazwa_pliku_csv = 'uczelnie_z_list.csv'

    # przykładowe dane
    dane_uczelni = [
        ['Collegium Da Vinci', 'ul. Kutrzeby 10', '61-719', 'Poznań'],
        ['Politechnika Warszawska', 'pl. Politechniki 1', '00-661', 'Warszawa'],
        ['Uniwersytet Warszawski', 'ul. Krakowskie Przedmieście 26/28', '00-927', 'Warszawa'],
        ['Warszawski Uniwersytet Medyczny', 'ul. Żwirki i Wigury 61', '02-091', 'Warszawa']
    ]
    tytuly_naglowkow = ['uczelnia', 'ulica', 'kod', 'miejscowość']

    print('ZAPISANE NAGŁÓWKI:')
    print(tytuly_naglowkow)
    print('ZAPISANE DANE:')
    print(*dane_uczelni, sep='\n')
    # zapis do pliku CSV
    listy_do_csv(nazwa_pliku_csv, dane_uczelni, tytuly_naglowkow)

    # odczyt z pliku CSV
    tytuly_naglowkow, dane_uczelni = csv_do_list(nazwa_pliku_csv)
    print('\nODCZYTANE NAGŁÓWKI:')
    print(tytuly_naglowkow)
    print('ODCZYTANE DANE:')
    print(*dane_uczelni, sep='\n')
