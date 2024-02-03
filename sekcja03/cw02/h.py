import re


def test_elementu_xml(xml):
    """
    Funkcja sprawdza, czy element o dopuszczalnej zawartości znakowej i bez atrybutów jest poprawny.

    :param xml: dane XML
    :return: True - jeśli element jest poprawny, w przeciwnym razie - False

    Element uznajemy za poprawny, jeśli znacznik otwierający ma odpowiadający mu znacznik domykający.
    """
    regex = r'<(.+?)>.*</\1>'
    wzorzec = re.compile(regex)
    return wzorzec.search(xml) is not None


if __name__ == '__main__':
    # xml = '<xxx>aaa</yyy>'
    # przykładowe dane testowe
    testowe_elementy_xml = [
        '<xxx>jakaś zawartość znakowa</xxx>',
        '<xxx></xxx>',
        '<xxx>jakaś zawartość znakowa</yyy>',
    ]

    print('CZY ELEMENT XML...                           JEST POPRAWNY?')
    print('-' * 60)
    for element_xml in testowe_elementy_xml:
        wynik_testu = test_elementu_xml(element_xml)
        print(f"{element_xml:45}{'TAK' if wynik_testu else 'NIE'}")
