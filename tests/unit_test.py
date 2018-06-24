import pytest
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from parse_utils import instruction_to_binary, parse_operand

def test_instruction_in_binary_handles_invalid_instruction_name():
    with pytest.raises(Exception, match=r'Invalid method name'):
        instruction_to_binary(["invalid name", "x"])

def test_instruction_in_binary_has_proper_length():
    test_cases = [
        ["add", "$s0", "$s1", "$s2"],
        ["addi", "$s0", "$s1", "$10"],
        ["addu", "$s0", "$s1", "$s2"],
        ["addiu", "$s0", "$s1", "$10"],
        ["and", "$s0", "$s1", "$s2"],
        ["andi", "$s0", "$s1", "$10"],
        ["lui", "$s0", "$10"],
        ["slti", "$s0", "$s1", "$10"],
        ["sltiu", "$s0", "$s1", "$10"],
        ["ori", "$s0", "$s1", "$10"],
        ["xori", "$s0", "$s1", "$10"],
        ["sll", "$s0", "$s1", "$10"],
        ["srl", "$s0", "$s1", "$10"],
        ["sra", "$s0", "$s1", "$10"],
        ["sllv", "$s0", "$s1", "$s2"],
        ["srlv", "$s0", "$s1", "$s2"],
        ["mfhi", "$s0"],
        ["mflo", "$s0"],
        ["mult", "$s0", "$s1"],
        ["multu", "$s0", "$s1"],
        ["div", "$s0", "$s1"],
        ["divu", "$s0", "$s1"],
        ["sub", "$s0", "$s1", "$s2"],
        ["subu", "$s0", "$s1", "$s2"],
        ["or", "$s0", "$s1", "$s2"],
        ["xor", "$s0", "$s1", "$s2"],
        ["slt", "$s0", "$s1", "$s2"],
        ["sltu", "$s0", "$s1", "$s2"],
        ["nor", "$s0", "$s1", "$s2"],
        ["srav", "$s0", "$s1", "$s2"],
        ["mthi", "$s0"],
        ["mtlo", "$s0"],
    ]

    for tC in test_cases:
        assert len(instruction_to_binary(tC)) == 32


def test_handle_parse_invalid_operand():
    with pytest.raises(Exception, match=r'Invalid operand'):
        parse_operand("abcd12")

def test_handle_parse_invalid_register_operand():
    with pytest.raises(Exception, match=r'Invalid operand'):
        parse_operand("$xyz")

def test_parse_operand_handles_negative_numbers():
    test_cases = {
        "-1": -1 & 0xffff,
        "-12345678": -12345678 & 0xffff,
    }

    for tC_key in test_cases:
        assert parse_operand(tC_key) == test_cases[tC_key]

def test_parse_valid_registers_operands():
    test_cases = {
        "$a1": 5,
        "$s1": 17,
        "$12": 12,
        "$5": 5,
    }

    for tC_key in test_cases:
        assert parse_operand(tC_key) == test_cases[tC_key]
