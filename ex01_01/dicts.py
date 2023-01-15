from csv import DictWriter, DictReader


def export_dicts_to_csv(csv_filename, data_dicts):
    header_names = data_dicts[0].keys()
    with open(csv_filename, mode='wt', encoding='utf-8', newline='') as file:
        writer = DictWriter(file, fieldnames=header_names)
        writer.writeheader()
        for single_dict in data_dicts:
            writer.writerow(single_dict)


def import_dicts_from_csv(csv_filename):
    with open(csv_filename, mode='rt', encoding='utf-8', newline='') as file:
        csv_reader = DictReader(file, delimiter=',')
        data_dicts = list(csv_reader)
    return data_dicts


if __name__ == '__main__':
    data = [
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

    export_dicts_to_csv('uczelnie2.csv', data)

    data = import_dicts_from_csv('uczelnie2.csv')
    print(*data, sep='\n')
