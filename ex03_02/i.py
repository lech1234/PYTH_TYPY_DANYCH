import re


# Lookahead - W stringu Jan Xxxxxx szukamy wszystkich Janów kończących się na ski, ale nie Kowalskich
def check_person(name):
    regex = '(Jan)(?=\s[A-Z][a-z]+ski)(?!\sKowalski)'

    pattern = re.compile(regex)
    match = pattern.search(name)
    if match:
        return match.group()

if __name__ == '__main__':
    test_names = 'Jan Sobieski', 'Jan Kowalski', 'Adam Nowakowski', 'Jan Adamowicz', 'Jan Kownacki', 'Jan Dynowski'

    for test_name in test_names:
        print(check_person(test_name))