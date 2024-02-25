from decimal import Decimal, ROUND_HALF_UP
import math
# # import sys
# sys.stdin = open("test.in", "r")

def solve():
    x = input().split()
    w = float(x[0])
    n = int(x[1])
    area = ((w/(2**n))**2*(math.sqrt(3)/4)*(3**n))

    print(str(3**n) +" "+ str(Decimal(area).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)))
for i in range(int(input())):
    solve()
