"""
--- Day 11: Corporate Policy ---
https://adventofcode.com/2015/day/11
"""
from aocd.models import Puzzle
import time


p = Puzzle(day=11, year=2015)
input = p.input_data
    
def increasing(password: str) -> bool:
    inc_count = 0
    curr = 0
    for char in password:
        if curr+1 == ord(char):
            curr = curr+1
            inc_count += 1
        else:
            curr = ord(char)
            inc_count = 1
        if inc_count > 2:
            return True
    return False

def not_allowed(password: str) -> bool:
    illegal = {'i', 'o', 'l'}
    for char in password:
        if char in illegal:
            return False
    return True

def non_overlap(password: str) -> bool:
    pair = set()
    prev = ""
    for char in password:
        if char == prev:
            pair.add(char)
            prev = ""
        else:
            prev = char
        if len(pair) > 1:
            return True
    return False

def increment(password: str) -> str:
    index = len(password)-1

    while password[index] == 'z':
        index -= 1
    
    return password[:index] + chr(ord(password[index])+1) + "a" * (len(password)-1-index)

while not (increasing(input) and not_allowed(input) and non_overlap(input)):
    input = increment(input)

p.answer_a = input