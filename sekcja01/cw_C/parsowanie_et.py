import xml.etree.ElementTree as ET

iterator = ET.iterparse('towary.xml', ['start', 'end'])

print('[początek dokumentu]')
for zdarzenie, element in iterator:
    match zdarzenie:
        case 'start':
            print(f'[znacznik otwierający]: element=\'{element.tag}\', atrybuty={element.attrib}')
        case 'end':
            print(f'[zawartość znakowa]   : {element.text!r}')
            print(f'[znacznik domykający] : element=\'{element.tag}\'')
print('[koniec dokumentu]')
