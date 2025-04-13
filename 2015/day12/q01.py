"""
--- Day 12: JSAbacusFramework.io ---
https://adventofcode.com/2015/day/12
"""
from aocd.models import Puzzle
import json


p = Puzzle(day=12, year=2015)
input = p.input_data

total = 0
is_neg = False
num = ""
for char in input:
    if char == '-':
        is_neg = True
    elif char.isdigit():
        num += char
    else:
        if num != "":
            total += -int(num) if is_neg else int(num)
        
        is_neg = False
        num = ""

p.answer_a = total