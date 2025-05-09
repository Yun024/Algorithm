import sys

input = sys.stdin.readline
num = 1
for _ in range(3):
    num *= int(input().strip())

ans = [0] * 10
for i in str(num):
    ans[int(i)] += 1

for i in ans:
    print(i)