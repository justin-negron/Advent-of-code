"""
--- Day 4: The Ideal Stocking Stuffer ---
https://adventofcode.com/2015/day/4
"""
from aocd.models import Puzzle
import sys
import hashlib


p = Puzzle(day=4, year=2015)
input = p.input_data

for i in range(sys.maxsize):
    low = input + str(i)
    low = low.encode('utf-8')
    md5 = hashlib.md5(low).hexdigest()
    if md5[:5] == "00000":
        p.answer_a = i
        break
