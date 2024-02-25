import sys
import math
# sys.stdin = open("test.in", "r")


def dist(rx, ry, x, y):
    return abs(math.sqrt((rx-x)**2 + (ry-y)**2))

def solve_test_case():
    num_points = int(input())
    rx,ry,safe_dist = map(int, input().split())

    for _ in range(num_points):
        x, y = map(int, input().split())
        
        d = dist(rx, ry, x, y)
        if d >= safe_dist:
            print(f"({x},{y})", "SAFE")
        else:
            print(f"({x},{y})", "DANGER")

for _ in range (int(input())):
    solve_test_case()