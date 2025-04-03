"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
https://adventofcode.com/2015/day/5
"""
from aocd.models import Puzzle


p = Puzzle(day=5, year=2015)
input = p.input_data.splitlines()

total_nice_strings = 0

for line in input:
    has_pair = False
    has_double = False
    possible_double = set()
    double_index = set()
    possible_double.add(line[0]+line[1])
    if line[0] == line[1]:
        double_index.add(1)
    for i in range(2, len(line)):
        if line[i-2] == line[i]:
            has_pair = True
        if line[i-1]+line[i] in possible_double and i-1 not in double_index:
            has_double = True
        if line[i-1] == line[i]:
            double_index.add(i-1)

    if has_pair and has_double:
        total_nice_strings += 1

p.answer_b = total_nice_strings
