# import sys
# sys.stdin = open("test.in", "r")

def solve_test_case():
    c, p = map(int, input().split())
    priority_map = {}

    for _ in range(c):
        ls = input().split()
        priority_map[ls[0]] = ls[1:]
    

    for _ in range(p):
        ls = input().split()
        sel_class = ls[0]
        dot = sorted([int(i) for i in ls[1:]])[::-1]

        print(sel_class)
        loop = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        for val in loop:
            
            priority = priority_map[sel_class].index(val)
            print(f"{val}: {dot[priority]}") 
        

            

for _ in range (int(input())):
    solve_test_case()