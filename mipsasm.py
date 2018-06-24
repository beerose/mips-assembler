#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import re

from parse_utils import to_hex, instruction_to_hex, instructions_names, output_template

def read_file(filename):
    file  = open(filename, "r")
    return file.readlines()

def parse_line(line, counter, comment=''):
    if len(line) > 2 and line[0] in instructions_names:
        hex_counter = '{:08x}'.format(counter)
        hex_instruction = instruction_to_hex(line)
        output = output_template.format(hex_counter, hex_instruction, line[0], ','.join(line[1:]))
        counter += 4
    else:
        return counter, ' '.join(line)
    return counter, output

def parse_file(args):
    counter = 0
    lines = read_file(args.file)
    for line in lines:
        output_format = '{0}'
        m = re.match(r'^([^#]*)#(.*)$', line)
        if m:  # The line contains a comment
            line = m.group(1)
            comment = '     #{0}'.format(m.group(2))
            output_format += comment
        counter, output = parse_line(line.rstrip().replace(',', ' ').split(), counter)
        print output_format.format(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file', '-f', 
        metavar='file_name',
        required=True,
        help='file with MIPS assembly code'
    )

    args = parser.parse_args()
    parse_file(args)
