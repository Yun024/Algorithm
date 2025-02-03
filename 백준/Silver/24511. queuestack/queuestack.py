import sys
input = sys.stdin.readline
from collections import deque
input()
struc = input().split()
num_list = input().split()
input()
w = input().split()[::-1]
z = deque([i for j,i in zip(struc,num_list) if j == '0'])
ans = []
while w:
    z.appendleft(w.pop())
    ans.append(z.pop())
print(*[int(i) for i in ans])