import yaml
from sekcja02.dane.model import *


def serializuj_do_yaml(obiekt):
    obiekt_zserializowany = yaml.dump(obiekt)
    return obiekt_zserializowany


def deserializuj_z_yaml(dane_yaml):
    obiekt_zdeserializowany = yaml.load(dane_yaml, Loader=yaml.Loader)
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

    kontakt_zserializowany = serializuj_do_yaml(kontakt)
    print('OBIEKT ZSERIALIZOWANY DO YAML:', kontakt_zserializowany, sep='\n')

    kontakt_zdeserializowany = deserializuj_z_yaml(kontakt_zserializowany)
    print('OBIEKT ZDESERIALIZOWANY Z YAML:', kontakt_zdeserializowany, sep='\n')
