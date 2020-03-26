#!/usr/bin/env python3

import sys
from os import listdir
from os.path import isfile


def wc(filename):
    line_counter = 0
    word_counter = 0
    letter_counter = 0

    file = open(filename, 'r')

    for line in file:
        line_counter += 1
        word_counter += len(line.split())
        letter_counter += len(line)
    file.close()

    print(line_counter, word_counter, letter_counter, filename)


if __name__ == "__main__":
    option = sys.argv[1]

    if option == "*":
        files = [f for f in listdir() if isfile(f)]
        for filename in files:
            wc(filename)

    elif option == "*.py":
        files = [f for f in listdir() if isfile(f) and f.split('.')[-1] == "py"]
        for filename in files:
            wc(filename)

    else:
        filename = option
        wc(filename)
