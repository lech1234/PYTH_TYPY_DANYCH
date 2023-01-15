import re


# Wyszukać wszystkie tagi użyte w xmlu
def find_tags(text):
    pattern = re.compile(r'<([^/].+?)>')
    tags = pattern.findall(text)
    print('Tags found:', tags)
    return tags


if __name__ == '__main__':
    xml = '<tag1> <tag2> abc </tag2></tag1>'
    find_tags(xml)
