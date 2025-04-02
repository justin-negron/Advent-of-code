"""
--- Day 1: Not Quite Lisp ---
https://adventofcode.com/2015/day/1
"""
from aocd.models import Puzzle


p = Puzzle(day=1, year=2015)
input = p.input_data

floors = input.count('(') - input.count(')')  

p.answer_a = floors

