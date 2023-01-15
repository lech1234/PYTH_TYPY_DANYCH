from ex02_data.model import *
from json import dumps, loads


def contact_to_json(contact):
    serialized = dumps(contact, default=vars)
    return serialized


def json_to_contact(contact):
    deserialized = loads(contact)
    deserialized['phones'] = [Phone(**phone) for phone in deserialized['phones']]
    return Contact(**deserialized)


if __name__ == '__main__':
    print('ORIGINAL PYTHON OBJECTS:', ct1, sep='\n')

    json_ct1 = contact_to_json(ct1)
    print('SERIALIZED TO JSON:', json_ct1, sep='\n')

    ct2 = json_to_contact(json_ct1)
    print('DESERIALIZED FROM JSON:', ct2, sep='\n')
