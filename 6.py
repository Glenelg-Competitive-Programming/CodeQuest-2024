# import sys
# sys.stdin = open("test.in", "r")

def solve_test_case():
    ip = input().split(".")

    if len(ip) != 4:
        print("INVALID")
        return
    
    for i in ip:
        if not i.isdecimal():
            print("INVALID")
            return
        if int(i) in range(0, 256):
            continue
        else:
            print("INVALID")
            return
    print("VALID")

for _ in range (int(input())):
    solve_test_case()