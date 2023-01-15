import re


# Lookahead - W stringu Jan Xxxxxx szukamy wszystkich Janów kończących się na ski, ale nie Kowalskich
def check_person(name):
    regex = '(?<=\d{11}\s)([A-Z][a-z]+sk[ai])'

    pattern = re.compile(regex)
    match = pattern.search(name)
    if match:
        return match.group()

if __name__ == '__main__':
    test_names = ('11111111111 Kowalski', '22222222222 Marecka', '33333333333 Nowakowska',
                  '44444444444 Szablewska', '55555555555 Wolski', '66666666666 Nowicki')

    for test_name in test_names:
        print(check_person(test_name))