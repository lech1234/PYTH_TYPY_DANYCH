from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('https://www.nbp.pl/home.aspx?f=/kursy/kursya.html')
html_page = response.read()

# parsowanie strony strony HTML
parsed_page = BeautifulSoup(html_page, 'html.parser')

# szukamy pierwszego znacznika H3
h3_tag = parsed_page.find('h3')
print(h3_tag.string)

# szukamy kolejnego elementu-rodzeństwa o nazwie 'table' z atrybutem 'class' o wartości 'nbptable',
# czyli tabeli kursów walut
currency_table_tag = h3_tag.find_next_sibling('table', class_='nbptable')
# print(currency_table_tag.prettify())

# wiersz nagłówka tabeli
headers_row_tag = currency_table_tag.thead.tr

# z wiersza nagłówków tabeli pobieramy ich nazwy
header_names = [header.string for header in headers_row_tag.find_all('th')]

# tworzymy listę w której znajdą się zczytane dane z tabeli
currency_list = []

table_contents_tag = currency_table_tag.tbody
for table_row_tag in table_contents_tag.find_all('tr'):
    row_values = [table_cell_tag.get_text() for table_cell_tag in table_row_tag.find_all('td')]
    currency_list.append(row_values)

print('{:40}{:30}{:30}'.format(*header_names))
for currency_data in currency_list:
    print('{:40}{:30}{:30}'.format(*currency_data))
