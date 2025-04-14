"""
--- Day 12: JSAbacusFramework.io ---
https://adventofcode.com/2015/day/12
"""
from aocd.models import Puzzle
import json


p = Puzzle(day=12, year=2015)
input = p.input_data

def recursum(input):
    match input:
        case dict():
            values = list(input.values())
            return 0 if "red" in values else recursum(values)
        case list():
            return sum(recursum(num) for num in input)
        case int():
            return input
        case _: return 0

p.answer_b = recursum(json.loads(input))