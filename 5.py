# import sys
# sys.stdin = open("test.in", "r")

from decimal import Decimal, ROUND_HALF_UP

def solve_test_case():

    num_parts = int(input())
    mn, sr, wr, pr, cr = map(int, input().split())

    total = sr+wr+pr+cr

    best_mn = mn

    for i in range(num_parts):
        mn1, sr, wr, pr, cr = map(int, input().split())
        if Decimal((sr + wr + pr + cr) * 1.2).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP) >= total:
            best_mn  =  mn1
            total = (sr+wr+pr+cr)

    print(f'{best_mn} {total}')
        

for _ in range (int(input())):
    solve_test_case()