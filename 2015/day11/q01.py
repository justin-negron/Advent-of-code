"""
--- Day 11: Corporate Policy ---
https://adventofcode.com/2015/day/11
"""
from aocd.models import Puzzle


p = Puzzle(day=11, year=2015)
input = p.input_data

input = "testzz"
    
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
    confirmed = set()
    possible = set()
    for char in password:
        if char in confirmed:
            pass
        elif char in possible:
            confirmed.add(char)
        else:
            possible.add(char)
        if len(confirmed) > 1:
            return True
    return False

def increment(password: str) -> str:
    index = len(password)-1

    if password[index] == 'z':
        index -= 1
    
    next_itr = password[:index] + chr(ord(password[index])+1) if ord(password[len(password)-1])+1 < 123 else password[:index] + chr(ord(password[index])+1) + "a"
    return next_itr


print(increasing(input))
print(not_allowed(input))
print(non_overlap(input))


print(increment(input))




# p.answer_a = 