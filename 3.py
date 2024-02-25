# import sys
from decimal import Decimal, ROUND_HALF_UP
# sys.stdin = open("test.in", "r")

def solve_test_case():
    x = int(input())
    if x <= 11000:
        print(Decimal(x*1.1-x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    elif x <= 44725:
        print(Decimal(x*1.12-x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    elif x <= 95375:
        print(Decimal(x * 1.22-x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    elif x<= 182100:
        print(Decimal(x * 1.24-x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    elif x<= 231250:
        print(Decimal(x * 1.32-x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    elif x <= 578125:
        print(Decimal(x * 1.35-x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    else:
        print(Decimal(x * 1.37-x).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


for _ in range (int(input())):
    solve_test_case()