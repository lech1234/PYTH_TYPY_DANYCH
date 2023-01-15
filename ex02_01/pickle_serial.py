from ex02_data.model import *
from pickle import dumps, loads


def contact_to_bytes(contact):
    serialized = dumps(contact)
    return serialized


def bytes_to_contact(bytes_contact):
    deserialized = loads(bytes_contact)
    return deserialized


if __name__ == '__main__':
    print('ORIGINAL PYTHON OBJECT:', ct1, sep='\n')

    bytes_ct1 = contact_to_bytes(ct1)
    print('SERIALIZED TO PICKLE:', bytes_ct1, sep='\n')

    ct2 = bytes_to_contact(bytes_ct1)
    print('DESERIALIZED FROM PICKLE:', ct2, sep='\n')
