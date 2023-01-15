import re


# czy dany tekst zaczyna się na ...
def has_prefix(full_text, prefix):
    regex = f'^{prefix}'

    pattern = re.compile(regex)
    match = pattern.search(full_text)
    check = match is not None
    full_text = "'" + full_text + "'"
    print(f"{full_text:15} begins with '{prefix}'? {check}")
    return check


if __name__ == '__main__':
    test_full_texts = 'abcfoo', 'fooabc', 'abcfooabc', ' foo '

    for test_full_text in test_full_texts:
        has_prefix(test_full_text, 'foo')
