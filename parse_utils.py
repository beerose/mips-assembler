#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

from instructions_templates import instructions_to_formats

instructions_names = ["add", "addi", "addu", "addiu", "and", "andi", "lui", "slti", "sltiu", "ori", "xori", "sll", "srl", "sra", "sllv", "srlv", "mfhi", "mflo", "mult", "multu", "div", "divu", "sub", "subu", "or", "xor", "slt", "sltu", "nor", "srav", "mthi", "mtlo"]

output_template = "{0}    {1}   {2}    {3}"

format_strings = {
    "OPCODE": "{:06b}",
    "REG": "{:05b}",
    "IMM": "{:016b}",
    "H": "{:05b}"
}

register_names_to_numbers = {
    "zero": 0,
    "at": 1,
    "v0": 2,
    "v1": 3,
    "a0": 4,
    "a1": 5,
    "a2": 6,
    "a3": 7,
    "t0": 8,
    "t1": 9,
    "t2": 10,
    "t3": 11,
    "t4": 12,
    "t5": 13,
    "t6": 14,
    "t7": 15,
    "s0": 16,
    "s1": 17,
    "s2": 18,
    "s3": 19,
    "s4": 20,
    "s5": 21,
    "s6": 22,
    "s7": 23,
    "t8": 24,
    "t9": 25,
    "k0": 26,
    "k1": 27,
    "gp": 28,
    "sp": 29,
    "fp": 30,
    "ra": 31,
}

to_hex = lambda s: '{:08x}'.format(int(s, 2))
number_regex = r'[\+\-]?[0-9]'

def parse_operand(operand):
    operand = operand.replace('$', '')
    if re.match(number_regex, operand):
        return int(operand) & 0xffff # because -12 is -1100 for python
    if operand not in register_names_to_numbers.keys():
        raise Exception("Invalid operand: {0}".format(operand))
    return register_names_to_numbers[operand]

def instruction_to_binary(line):
    if len(line) < 2:
        raise Exception("Invalid line: {0}".format(line))

    instruction_name = line[0]
    if instruction_name not in instructions_to_formats:
        raise Exception("Invalid method name: {0}".format(instruction_name))

    operandTypes, operandsTemplate = instructions_to_formats[instruction_name]
    
    return operandsTemplate.format(
        *[format_strings[t].format(parse_operand(line[i + 1])) for i, t in enumerate(operandTypes)]
    )
    
def instruction_to_hex(line):
    return to_hex(instruction_to_binary(line))
