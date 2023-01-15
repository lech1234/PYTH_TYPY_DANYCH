from ex02_data.model import *
from yaml import dump, load, Loader


def contact_to_yaml(contact):
    serialized = dump(contact)
    return serialized


def yaml_to_contact(yaml_contact):
    deserialized = load(yaml_contact, Loader=Loader)
    return deserialized


if __name__ == '__main__':
    print('ORIGINAL PYTHON OBJECT:', ct1, sep='\n')

    yaml_ct1 = contact_to_yaml(ct1)
    print('SERIALIZED TO YAML:', yaml_ct1, sep='\n')

    ct2 = yaml_to_contact(yaml_ct1)
    print('DESERIALIZED FROM YAML:', ct2, sep='\n')
