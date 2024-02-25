# import sys
# sys.stdin = open("test.in", "r")

def solve_test_case():

    ls = [("AEILNORSTU",1), ("DG", 2), ("BCMP", 3), ("FHVWY", 4), ("K", 5), ("JX", 8), ("QZ", 10)]

    p = input()
    s=0
    for char in p:
        point = [i[1] for i in ls if char in i[0]][0]
        print(f"{char}={point}")
        s+=point
    print(f"TOTAL={s}")

for _ in range (int(input())):
    solve_test_case()