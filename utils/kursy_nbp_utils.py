def utworz_tytul_tabeli(numer_tabeli, data_tabeli):
    return f'Tabela nr {numer_tabeli} z dnia {data_tabeli}'


def wypisz_tabele_kursow(tytul_tabeli, tabela_kursow):
    print(tytul_tabeli.upper())
    print('-' * 65)
    print(f'{"Nazwa waluty":40}{"Kod waluty":>10}{"Kurs średni":>15}')
    print('-' * 65)

    for waluta in tabela_kursow:
        print('{currency:40}{code:>10}{mid:>15}'.format(**waluta))
