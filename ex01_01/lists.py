from csv import writer, reader


def export_lists_to_csv(csv_filename, data_lists, header_names):
    with open(csv_filename, mode='wt', encoding='utf-8', newline='') as file:
        csv_writer = writer(file, delimiter=',')
        csv_writer.writerow(header_names)
        for data_list in data_lists:
            csv_writer.writerow(data_list)


def import_lists_from_csv(csv_filename):
    with open(csv_filename, mode='rt', encoding='utf-8', newline='') as file:
        csv_reader = reader(file, delimiter=',')
        header_names, *data_lists = list(csv_reader)
    return header_names, data_lists


if __name__ == '__main__':
    data = [
        ['Politechnika Warszawska', 'pl. Politechniki 1', '00-661', 'Warszawa'],
        ['Uniwersytet Warszawski', 'ul. Krakowskie Przedmieście 26/28', '00-927', 'Warszawa'],
        ['Warszawski Uniwersytet Medyczny', 'ul. Żwirki i Wigury 61', '02-091', 'Warszawa']
    ]
    header_names = ['uczelnia', 'ulica', 'kod', 'miejscowość']

    # zapis do pliku CSV
    export_lists_to_csv('uczelnie1.csv', data, header_names)

    # odczyt z pliku CSV
    header_names, data = import_lists_from_csv('uczelnie1.csv')
    print('Nagłówki:')
    print(header_names)
    print('Dane:')
    print(*data, sep='\n')
