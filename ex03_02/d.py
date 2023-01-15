import re


# czy tekst jest prostym adresem e-mail o~postaci: xxx@xxx.xxx
def is_correct_email(phone_number):
    # ^\w{3}@\w{3}\.(?:com|pl|gov)$
    regex = r'^\w{3}@\w{3}\.\w{3}$'

    pattern = re.compile(regex)
    match = pattern.search(phone_number)
    check = match is not None
    text = '"' + phone_number + '"'
    print(f'{text:15} is correct e-mail? {check}')
    return check


if __name__ == '__main__':
    test_emails = 'abc@def.com', 'abc@def.pl', 'abc@defxghi', 'abc@123.gov'

    for test_email in test_emails:
        is_correct_email(test_email)
