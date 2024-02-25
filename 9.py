# import sys
from decimal import Decimal, ROUND_HALF_UP
# sys.stdin = open("test.in", "r")

def solve_test_case():
    x = input().split()
    m = int(x[0])
    s = int(x[1])
    diction = {}
    for p in range(m):
        y = input().split()
        diction[y[0]] = float(y[1])
    for p in range(s):
        z = input().split()
        total = float(z[2])-diction[z[0]]*float(z[1])
        if total <= 0:
            print("Infinity")
        else:
            print(Decimal(50/total).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

for _ in range (int(input())):
    solve_test_case()