"""
--- Day 8: Matchsticks ---
https://adventofcode.com/2015/day/8
"""
from aocd.models import Puzzle


p = Puzzle(day=8, year=2015)
input = p.input_data.splitlines()

total_literals = 0
total_enc_literals = 0

def encode(line):
    enc_len = 0
    for i in range(len(line)):
        if line[i] == "\"" or line[i] == "\\":
            enc_len += 2
        else:
            enc_len += 1
    return enc_len+2
    

for line in input:
    total_literals += len(line)
    total_enc_literals += encode(line)

p.answer_b = total_enc_literals - total_literals