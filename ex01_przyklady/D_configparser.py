# odczyt parametrów konfiguracyjnych z pliku za pomocą configparser

from configparser import ConfigParser

config = ConfigParser()
config.read('db.ini')
print('Sections:', config.sections())

for section_name in config.sections():
    section = config[section_name]
    print(section)
    for key in section.keys():
        print(f'\t{key}: {section[key]}')
