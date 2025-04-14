"""
--- Day 13: Knights of the Dinner Table ---
https://adventofcode.com/2015/day/13
"""
from aocd.models import Puzzle


p = Puzzle(day=13,year=2015)
input = p.input_data.splitlines()

for line in input:
    p1, _, mood, points, _, _, _, _, _, _, p2 = line[:-1].split()
    print(p1, mood, points, p2)

# p.answer_a = 