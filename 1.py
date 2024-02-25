# import sys
# sys.stdin = open("test.in", "r")
from collections import Counter

def solve_test_case():
    word = input()
    word = word.replace(" ", "")

    h = dict(Counter(word))
    print(max(list(h.values())))

for _ in range (int(input())):
    solve_test_case()