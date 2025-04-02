"""
--- Day 2: I Was Told There Would Be No Math ---
https://adventofcode.com/2015/day/2
"""
from aocd.models import Puzzle


p = Puzzle(day=2, year=2015)
input = p.input_data.splitlines()

wrap = 0

for line in input:
    nums = [int(n) for n in line.split("x")]
    min_area = min(nums[0]*nums[1], nums[1]*nums[2], nums[0]*nums[2])
    wrap += 2*nums[0]*nums[1] + 2*nums[1]*nums[2] + 2*nums[0]*nums[2] + min_area

p.answer_a = wrap