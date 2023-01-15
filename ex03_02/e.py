import re


# czy tekst jest 4- lub 5-znakowym palindromem?
def is_palindrome(text):
    regex = r'^([a-z])([a-z])[a-z]?\2\1$'

    pattern = re.compile(regex, flags=re.I)
    match = pattern.search(text)
    check = match is not None
    print(f"'{text}' is palindrome? {check}")
    return check


if __name__ == '__main__':
    test_palindromes = 'kayak', 'cocoa', 'radar', 'Abba'

    for test_palindrome in test_palindromes:
        is_palindrome(test_palindrome)
