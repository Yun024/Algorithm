import sys
input = sys.stdin.readline

n = int(input().strip())
O_cnt = input().strip().count("O")
if n%2:
    print("Yes" if n//2 < O_cnt else "No")
else:
    print("Yes" if n//2 <= O_cnt else "No")
    