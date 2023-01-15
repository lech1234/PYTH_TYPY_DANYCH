import re


# czy dany tekst kończy się na ...
def has_suffix(full_text, suffix):
    regex = f'{suffix}$'

    pattern = re.compile(regex)
    match = pattern.search(full_text)
    check = match is not None
    full_text = "'" + full_text + "'"
    print(f"{full_text:15} ends with '{suffix}'? {check}")
    return check


if __name__ == '__main__':
    test_full_texts = 'abcfoo', 'fooabc', 'abcfooabc', ' foo '

    for test_full_text in test_full_texts:
        has_suffix(test_full_text, 'foo')
