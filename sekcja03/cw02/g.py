import re


def znajdz_elementy_w_xml(xml_data):
    """
    Funkcja wyszukuje nazwy elementów w danych XML.

    :param xml_data: dane XML
    :return: lista nazw elementów
    """
    regex = r'<([^/?!].+?)[ >]'
    wzorzec = re.compile(regex)
    return wzorzec.findall(xml_data)


if __name__ == '__main__':
    # przykładowe dane XML
    xml = '''<?xml version="1.0" encoding="utf-8" ?>
<!-- Lista towarów -->
<towary>
    <towar id="PN12345">
        <nazwa>klin</nazwa>
        <ilosc>10</ilosc>
    </towar>
    <towar id="PN54321">
        <nazwa>cokół</nazwa>
        <ilosc>7</ilosc>
    </towar>
</towary>'''

    elementy = znajdz_elementy_w_xml(xml)
    print('ZNALEZIONE ELEMENTY:')
    print(*elementy, sep='\n')
