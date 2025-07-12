import sys
input = sys.stdin.readline
S = input().strip()
print(min(len([i for i in S.split("1") if i]), len([i for i in S.split("0") if i])))