import pytest
import sys, os, subprocess
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

import mipsasm

for i in range (1, 5):
    cmd = "python mipsasm.py --file tests/test{0}.in".format(i).split()
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE ).communicate()[0].split("\n")[:-1]

    file  = open("tests/test{0}.in".format(i), "r")
    lines = file.readlines()

    print i
    assert len(lines) == len (output)
    for i, line in enumerate(lines):
        for word in line.rstrip().replace(',', ' ').split():
            assert word in output[i].replace(',', ' ').split()
