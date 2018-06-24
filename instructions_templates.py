REG = "REG"
IMM = "IMM"
H = "H"

# maping from instriction to [[operands types], [opcode, encoding template]]
instructions_to_formats = {
    # add $d, $s, $t            $d = $s + $t
    # encoding: 0000 00ss ssst tttt dddd d000 0010 0000
    "add": [[REG, REG, REG], "000000{1}{2}{0}00000100000"],
    # addi $t, $s, imm          $t = $s + imm
    # encoding: 0010 00ss ssst tttt iiii iiii iiii iiii
    "addi": [[REG, REG, IMM], "001000{1}{0}{2}"],
    # addu $d, $s, $t           $d = $s + $t
    # Encoding: 0000 00ss ssst tttt dddd d000 0010 0001
    "addu": [[REG, REG, REG], "000000{1}{2}{0}00000100001"],
    # addiu $t, $s, imm
    # Encoding: 0010 01ss ssst tttt iiii iiii iiii iiii
    "addiu": [[REG, REG, IMM], "001001{1}{0}{2}"],
    # and $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d000 0010 0100
    "and": [[REG, REG, REG], "000000{1}{2}{0}00000100100"],
    # andi $t, $s, imm
    # Encoding: 0011 00ss ssst tttt iiii iiii iiii iiii
    "andi": [[REG, REG, IMM], "001100{1}{0}{2}"],
    # lui $t, imm
    # Encoding: 0011 11-- ---t tttt iiii iiii iiii iiii
    "lui": [[REG, IMM], "00111100000{0}{1}"],
    # slti $t, $s, imm
    # Encoding: 0010 10ss ssst tttt iiii iiii iiii iiii
    "slti": [[REG, REG, IMM], "001010{1}{0}{2}"],
    # sltiu $t, $s, imm
    # Encoding: 0010 11ss ssst tttt iiii iiii iiii iiii
    "sltiu": [[REG, REG, IMM], "001011{1}{0}{2}"],
    # ori $t, $s, imm
    # Encoding: 0011 01ss ssst tttt iiii iiii iiii iiii
    "ori": [[REG, REG, IMM], "001101{1}{0}{2}"],
    # xori $t, $s, imm
    # Encoding: 0011 10ss ssst tttt iiii iiii iiii iiii
    "xori": [[REG, REG, IMM], "001110{1}{0}{2}"],
    # sll $d, $t, h
    # Encoding: 0000 00-- ---t tttt dddd dhhh hh00 0000
    "sll": [[REG, REG, H], "00000000000{1}{0}{2}000000"],
    # srl $d, $t, h
    # Encoding: 0000 00-- ---t tttt dddd dhhh hh00 0010
    "srl": [[REG, REG, H], "00000000000{1}{0}{2}000010"],
    # sra $d, $t, h
    # Encoding: 0000 00-- ---t tttt dddd dhhh hh00 0011
    "sra": [[REG, REG, H], "00000000000{1}{0}{2}000011"],
    # sllv $d, $t, $s
    # Encoding: 0000 00ss ssst tttt dddd d--- --00 0100
    "sllv": [[REG, REG, REG], "000000{2}{1}{0}00000000100"],
    # srlv $d, $t, $s
    # Encoding: 0000 00ss ssst tttt dddd d000 0000 0110
    "srlv": [[REG, REG, REG], "000000{2}{1}{0}00000000110"],
    # mfhi $d
    # Encoding: 0000 0000 0000 0000 dddd d000 0001 0000
    "mfhi": [[REG], "0000000000000000{0}00000010000"],
    # mflo $d
    # Encoding: 0000 0000 0000 0000 dddd d000 0001 0010
    "mflo": [[REG], "0000000000000000{0}00000010010"],
    # mult $s, $t
    # Encoding: 0000 00ss ssst tttt 0000 0000 0001 1000
    "mult": [[REG, REG], "000000{0}{1}0000000000011000"],
    # multu $s, $t
    # Encoding: 0000 00ss ssst tttt 0000 0000 0001 1001
    "multu": [[REG, REG], "000000{0}{1}0000000000011001"],
    # div $s, $t
    # Encoding: 0000 00ss ssst tttt 0000 0000 0001 1010
    "div": [[REG, REG], "000000{0}{1}0000000000011010"],
    # divu $s, $t
    # Encoding: 0000 00ss ssst tttt 0000 0000 0001 1000
    "divu": [[REG, REG], "000000{0}{1}0000000000011011"],
    # sub $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d000 0010 0010
    "sub": [[REG, REG, REG], "000000{1}{2}{0}00000100010"],
    # subu $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d000 0010 0011
    "subu": [[REG, REG, REG], "000000{1}{2}{0}00000100011"],
    # or $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d000 0010 0101
    "or": [[REG, REG, REG], "000000{1}{2}{0}00000100101"],
    # xor $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d--- --10 0110
    "xor": [[REG, REG, REG], "000000{1}{2}{0}00000100110"],
    # slt $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d000 0010 1010
    "slt": [[REG, REG, REG], "000000{1}{2}{0}00000101010"],
    # sltu $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d000 0010 1011
    "sltu": [[REG, REG, REG], "000000{1}{2}{0}00000101011"],
    # nor $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d--- --10 0111
    "nor": [[REG, REG, REG], "000000{1}{2}{0}00000100111"],
    # srav $d, $s, $t
    # Encoding: 0000 00ss ssst tttt dddd d--- --00 0111
    "srav": [[REG, REG, REG], "000000{1}{2}{0}00000000111"],
    # mthi $s
    # Encoding: 0000 00ss sss- ---- ---- ---- --01 0001
    "mthi": [[REG], "000000{0}000000000000000010001"],
    # mtlo $s
    # Encoding: 0000 00ss sss- ---- ---- ---- --01 0011
    "mtlo": [[REG], "000000{0}000000000000000010011"],
}
