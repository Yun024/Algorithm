import sys

input = sys.stdin.readline

S = input().strip()
n = int(input().strip())

for _ in range(n):
    alpha, l, r = input().split()
    print(len([i for i in S[int(l):int(r)+1] if i == alpha]))
