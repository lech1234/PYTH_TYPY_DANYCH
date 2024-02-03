from csv import DictWriter, DictReader


def slowniki_do_csv(plik_csv, slowniki):
    """
    Funkcja zapisuje dane ze słowników (o spójnym zestawie kluczy) do pliku CSV.

    :param plik_csv: nazwa i położenie pliku CSV
    :param slowniki: sekwencja słowników
    :return: None
    """
    tytuly_naglowkow = slowniki[0].keys()
    with open(plik_csv, mode='wt', encoding='utf-8', newline='') as plik:
        writer = DictWriter(plik, fieldnames=tytuly_naglowkow)
        writer.writeheader()
        for slownik in slowniki:
            writer.writerow(slownik)


def csv_do_slownikow(plik_csv):
    """
    Funkcja tworzy listę słowników zawierających dane z pliku CSV.

    :param plik_csv: nazwa i położenie pliku CSV
    :return: lista słowników z kluczami odpowiadającymi nazwom nagłówków w pliku CSV
    """
    with open(plik_csv, mode='rt', encoding='utf-8', newline='') as plik:
        csv_reader = DictReader(plik, delimiter=',')
        slowniki = list(csv_reader)
    return slowniki


if __name__ == '__main__':
    nazwa_pliku_csv = 'uczelnie_ze_slownikow.csv'

    # przykładowe dane
    dane_uczelni = [
        {
            'uczelnia': 'Collegium Da Vinci',
            'ulica': 'ul. Kutrzeby 10',
            'kod': '61-719',
            'miejscowosc': 'Poznań'
        },
        {
            'uczelnia': 'Politechnika Warszawska',
            'ulica': 'pl. Politechniki 1',
            'kod': '00-661',
            'miejscowosc': 'Warszawa'
        },
        {
            'uczelnia': 'Uniwersytet Warszawski',
            'ulica': 'ul. Krakowskie Przedmieście 26/28',
            'kod': '00-927',
            'miejscowosc': 'Warszawa'
        },
        {
            'uczelnia': 'Warszawski Uniwersytet Medyczny',
            'ulica': 'ul. Żwirki i Wigury 61',
            'kod': '02-091',
            'miejscowosc': 'Warszawa'
        }
    ]

    print('ZAPISANE DANE:')
    print(*dane_uczelni, sep='\n')
    slowniki_do_csv(nazwa_pliku_csv, dane_uczelni)

    dane_uczelni = csv_do_slownikow(nazwa_pliku_csv)
    print('\nODCZYTANE DANE:')
    print(*dane_uczelni, sep='\n')
