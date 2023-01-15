# odczyt parametrów i opcji za pomocą listy sys.argv

import sys

for nr, arg in enumerate(sys.argv):
    print(f'argv[{nr}] = {arg}')
