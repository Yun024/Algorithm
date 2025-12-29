import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
price = [int(input().strip()) for _ in range(n)]
weight = {idx+1:int(input().strip()) for idx in range(m)}
ans, parking, wait = 0,[0]*n,deque()

for _ in range(2*m):
    temp = int(input().strip())
    if temp > 0:
        for i in range(n):
            if not parking[i]:
                parking[i] = temp
                break
        else:
            wait.append(temp)
    else:
        abs_temp = abs(temp)
        pop_idx = parking.index(abs_temp)
        parking[pop_idx]=0
        for i in range(n):
            if not parking[i] and wait:
                parking[i] = wait.popleft()
        ans += price[pop_idx] * weight[abs_temp]

print(ans)