import re


# Lookahead - W stringu Jan Xxxxxx szukamy wszystkich Janów kończących się na ski, ale nie Kowalskich
def sprawdz_osobe(pesel_z_nazwiskiem):
    regex = r'(?<=\d{11}\s)([A-Z][a-z]*sk[ai])'

    wzorzec = re.compile(regex)
    dopasowanie = wzorzec.search(pesel_z_nazwiskiem)
    if dopasowanie:
        return dopasowanie.group()


if __name__ == '__main__':
    dane_testowe = [
        '11111111111 Kowalski',
        '22222222222 Marecka',
        '3333333333 Nowakowska',
        '44444444444 Szablewska',
        '55555555555 Wolski',
        '666666666666 Nowicki'
    ]

    print(f'{"DANE":30}WYNIK WYSZUKANIA')
    print('-'*50)
    for dana_testowa in dane_testowe:
        wynik = sprawdz_osobe(dana_testowa)
        print(f'{dana_testowa:30}{wynik if wynik else "-"}')
