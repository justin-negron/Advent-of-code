"""
--- Day 2: I Was Told There Would Be No Math ---
https://adventofcode.com/2015/day/2
"""
from aocd.models import Puzzle


p = Puzzle(day=2, year=2015)
input = p.input_data.splitlines()

rib = 0

for line in input:
    nums = [int(n) for n in line.split("x")]
    cub = nums[0]*nums[1]*nums[2]
    rib += 2*min(nums[0]+nums[1], nums[1]+nums[2], nums[0]+nums[2])+cub

p.answer_b = rib