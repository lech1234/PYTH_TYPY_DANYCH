import yaml


def serializuj_do_yaml(nazwa_pliku, obiekt):
    with open(nazwa_pliku, mode='wt', encoding='utf-8') as plik:
        yaml.dump(obiekt, plik, sort_keys=False, default_flow_style=False, allow_unicode=True)


def deserializuj_z_yaml(nazwa_pliku):
    with open(nazwa_pliku, mode='rt', encoding='utf-8') as plik:
        obiekt = yaml.load(plik, Loader=yaml.SafeLoader)
        return obiekt


if __name__ == '__main__':
    from pprint import pprint

    dane_testowe = [
        {
            'kod': 'PYTH01',
            'nazwa': 'Podstawy programowania w języku Python',
            'poziom': 1
        },
        {
            'kod': 'PYTH02',
            'nazwa': 'Zaawansowane techniki programowania w języku Python',
            'poziom': 2
        }
    ]

    plik_testowy = 'szkolenia.yaml'

    print('DANE PRZED SERIALIZACJĄ:')
    pprint(dane_testowe)

    serializuj_do_yaml(plik_testowy, dane_testowe)
    dane_po_deserializacji = deserializuj_z_yaml(plik_testowy)

    print('\nDANE PO DESERIALIZACJI:')
    pprint(dane_po_deserializacji)

    print('\nCZY RÓWNE?', dane_testowe == dane_po_deserializacji)
