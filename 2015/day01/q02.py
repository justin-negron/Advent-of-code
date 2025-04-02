"""
--- Day 1: Not Quite Lisp ---
https://adventofcode.com/2015/day/1
"""
from aocd.models import Puzzle


p = Puzzle(day=1, year=2015)
input = p.input_data

floors = 0

for i, par in enumerate(input, start=1):
    floors += 1 if par == '(' else -1
    if floors < 0:
        p.answer_b = i
        break
