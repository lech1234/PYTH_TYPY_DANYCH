import re


# czy ktoś się jąka -- powtórzone co najmniej 2 litery
def is_stuttering(text):
    pattern = re.compile(r'[a-z]*([a-z])\1[a-z]*')
    match = pattern.search(text)
    check = match is not None
    text = "'" + text + "'"
    print(f"{text:14} is stuttering? {check}")
    return check


if __name__ == '__main__':
    test_stuttering_texts = 'stutter', 'cocoa', 'apple', 'halloween', 'aardvark'

    for test_stuttering_text in test_stuttering_texts:
        is_stuttering(test_stuttering_text)
