# odczyt parametrów i opcji za pomocą argparse

from argparse import ArgumentParser

parser = ArgumentParser(
    prog='B_tail',
    description='Program is used to print a given number of last lines')

parser.add_argument('file')  # positional argument
parser.add_argument('-l', '--lines', type=int, default=10)  # option that takes a value
parser.add_argument('--enumerate', action='store_true')  # on/off flag
args = parser.parse_args()

print('Argument pozycyjny  : file =', args.file)
print('Argument nazwany    : lines =', args.lines)
print('Flaga               : enumerate =', args.enumerate)
print('Sparsowane argumenty:', args)
