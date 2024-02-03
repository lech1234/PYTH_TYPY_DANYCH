import pickle


def serializuj_do_pickle(nazwa_pliku, obiekt):
    with open(nazwa_pliku, mode='wb') as plik:
        pickle.dump(obiekt, plik)


def deserializuj_z_pickle(nazwa_pliku):
    with open(nazwa_pliku, mode='rb') as plik:
        obiekt = pickle.load(plik)
    return obiekt


if __name__ == '__main__':
    from pprint import pprint

    plik_testowy = 'dane.pkl'

    dane_przed_serializacja = {
        'a': [1, 2.0, True],
        'b': ('jakiś tekst', 'żółw'.encode('utf-8')),
        'c': None
    }
    print('DANE PRZED SERIALIZACJĄ:')
    pprint(dane_przed_serializacja)

    serializuj_do_pickle(plik_testowy, dane_przed_serializacja)
    dane_po_deserializacji = deserializuj_z_pickle(plik_testowy)

    print('\nDANE PO DESERIALIZACJI:')
    pprint(dane_po_deserializacji)

    print('\nCZY RÓWNE?', dane_przed_serializacja == dane_po_deserializacji)