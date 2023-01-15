# odczyt parametrów i opcji za pomocą getopt

import getopt
import sys

command_line_args = sys.argv[1:]
option_list, argument_list = getopt.getopt(command_line_args,
                                           'l:', ['lines=', 'enumerate'])
print('Lista opcji:     ', option_list)
print('Lista argumentów:', argument_list)
