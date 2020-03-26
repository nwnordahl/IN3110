#!/usr/bin/env python3

import sys

filename = sys.argv[1]
file = open(f'{filename}', 'r')

line_counter = 0
word_counter = 0
letter_counter = 0

for line in file:
    word_list = line.split()
    line_counter += 1
    word_counter += len(word_list)
    letter_counter += len(line)
file.close()

print(line_counter, word_counter, letter_counter, filename)
