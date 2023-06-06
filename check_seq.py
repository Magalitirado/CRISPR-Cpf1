import sys

def check_seq(seq):
    for i in seq:
        if i == '\n':
            print('This file contains line breaks, that will interfere with crRNA analysis.\nPlease remove them before running the program.\n')
            sys.exit()
        elif i not in ['a','t','c','g']:
            print('This genome is not only containing nucleotides...\n')
            sys.exit()
