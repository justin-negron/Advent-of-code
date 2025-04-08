"""
--- Day 7: Some Assembly Required ---
https://adventofcode.com/2015/day/7
"""
from aocd.models import Puzzle
from collections import deque
import numpy as np


p = Puzzle(day=7, year=2015)
input = p.input_data.splitlines()
q = deque(input)
var_map = dict()

def get(var):
    return var_map[var] if var in var_map else np.uint16(var)

while q:
    line = q.pop()
    try:
        match line.split():
            case n, "->", w:
                var_map[w] = get(n)
            case "NOT", n, "->", w:
                var_map[w] = ~get(n)
            case x, op, y, "->", w:
                f = getattr(np.uint16, f"__{op}__".lower())
                var_map[w] = f(get(x), get(y))
    except (KeyError, ValueError):
        q.appendleft(line)

p.answer_a = var_map["a"]