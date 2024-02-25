import sys
from decimal import Decimal, ROUND_HALF_UP
# sys.stdin = open("test.in", "r")

def solve_test_case():
    v1, m1, v2, m2 = map(float, input().split(","))

    V = (m1*v1 + m2*v2)/(m1+m2)

    V = Decimal(V).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    print("%.2f" % V)

for _ in range (int(input())):
    solve_test_case()