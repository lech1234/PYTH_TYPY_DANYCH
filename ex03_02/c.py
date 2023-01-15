import re


# czy tekst reprezentuje poprawny numer telefonu komórkowego w PL: +48xxxxxxxxx
def is_correct_phone_number(phone_number):
    regex = r'^\+48\d{9}$'
    pattern = re.compile(regex)
    match = pattern.search(phone_number)
    check = match is not None
    text = "'" + phone_number + "'"
    print(f"{text:15} is correct phone number? {check}")
    return check


if __name__ == '__main__':
    test_phone_numbers = '+481234567890', '+48123456789', '+14812345678', ' +48123456789'

    for test_phone_number in test_phone_numbers:
        is_correct_phone_number(test_phone_number)
