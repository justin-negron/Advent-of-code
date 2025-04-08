"""
--- Day 8: Matchsticks ---
https://adventofcode.com/2015/day/8
"""
from aocd.models import Puzzle


p = Puzzle(day=8, year=2015)
input = p.input_data.splitlines()

total_literals = 0
total_memory = 0

for line in input:
    total_literals += len(line)
    i = 1
    while i < len(line)-1:
        if line[i] == "\\" and line[i+1] == "x":
            total_memory += 1
            i += 4
        elif line[i] == "\\" and i+1 != len(line):
            total_memory += 1
            i += 2
        else:
            total_memory += 1
            i += 1

p.answer_a = total_literals - total_memory