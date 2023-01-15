import re


# Sprawdzić poprawność xml'a: <xxx>aaa</yyy>
def check_tags(xml):
    regex = r'<(.+?)>.*</\1>'

    pattern = re.compile(regex)
    match = pattern.search(xml)
    check = match is not None
    print('XML is correct:', check)
    return check


if __name__ == '__main__':
    xml = '<xxx>aaa</yyy>'
    check_tags(xml)
