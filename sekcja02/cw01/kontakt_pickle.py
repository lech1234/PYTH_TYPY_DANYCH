from sekcja02.dane.model import *
from pickle import dumps, loads


def serializuj_do_bytes(obiekt):
    """
    Funkcja serializuje obiekt do obiektu typu bytes.

    :param obiekt: serializowany obiekt
    :return: obiekt typu bytes
    """
    obiekt_zserializowany = dumps(obiekt)
    return obiekt_zserializowany


def deserializuj_z_bytes(obiekt):
    """
    Funkcja deserializuje obiekt na podstawie danych typu bytes.

    :param obiekt: obiekt typu bytes
    :return: zdeserializowany obiekt
    """
    obiekt_zdeserializowany = loads(obiekt)
    return obiekt_zdeserializowany


if __name__ == '__main__':
    # przykładowe dane
    kontakt = Kontakt('Jan',
                      'Kowalski',
                      [
                          Telefon('służbowy', '123456789'),
                          Telefon('prywatny', '987654321')
                      ]
                      )
    print('ORYGINALNY OBIEKT PYTHONA:', kontakt, sep='\n', end='\n\n')

    kontakt_zserializowany = serializuj_do_bytes(kontakt)
    print('OBIEKT ZSERIALIZOWANY DO bytes:', kontakt_zserializowany, sep='\n', end='\n\n')

    kontakt_zdeserializowany = deserializuj_z_bytes(kontakt_zserializowany)
    print('OBIEKT ZDESERIALIZOWANY Z bytes:', kontakt_zdeserializowany, sep='\n')
