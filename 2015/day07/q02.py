"""
--- Day 7: Some Assembly Required ---
https://adventofcode.com/2015/day/7
"""
from aocd.models import Puzzle
from collections import deque
import numpy as np


p = Puzzle(day=7, year=2015)
input = p.input_data.splitlines()

var_map = dict()

def assembly(q, wire):
    
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

    return var_map[wire]

# take signal of wire a
wire_a = assembly(deque(input), "a")
# reset other wires
var_map = dict()
# override wire b with previous wire a
var_map["b"] = wire_a
# what is new signal of wire a?
p.answer_b = assembly(deque(input), "a")