import json


def serializuj_do_json(obiekt):
    return json.dumps(obiekt)


def deserializuj_z_json(dane_json):
    obiekt = json.loads(dane_json)
    return obiekt


if __name__ == '__main__':
    dane_testowe = ['Jan Kowalski',
                    {
                        'adres': ('ul. Morska 123', '82-103', 'Stegna'),
                        'inne_dane': (None, 1, 2.0, False)
                    }
                    ]
    print('DANE PRZED SERIALIZACJĄ:')
    print(dane_testowe)

    dane_zserializowane = serializuj_do_json(dane_testowe)
    print('\nDANE ZSERIALIZOWANE (JSON):')
    print(dane_zserializowane)

    dane_po_deserializacji = deserializuj_z_json(dane_zserializowane)
    print('\nDANE PO DESERIALIZACJI:')
    print(dane_po_deserializacji)

    print('\nCZY RÓWNE?', dane_testowe == dane_po_deserializacji)
