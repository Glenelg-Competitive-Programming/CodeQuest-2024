import sys
from functools import cmp_to_key
# sys.stdin = open("test.in", "r")
def compare(x, y):
    p = min(len(x), len(y))

    for i in range(p):
        val_x = int(x[i])
        val_y = int(y[i])

        if val_y > val_x:
            return -1
        if val_x > val_y:
            return 1
    if len(x) == len(y):
        return 0
    elif (len(x) < len(y)):
        return 1
    else:
        return -1
    
def solve_test_case():
    ls = input().split()

    ls = sorted(ls, key = cmp_to_key(compare))[::-1]

    print("".join(ls))
    
    

for _ in range (int(input())):
    solve_test_case()