from collections import deque
n = int(input())
ans = deque([i for i in range(1,n+1)])
while len(ans) != 1:
    ans.popleft()
    ans.append(ans.popleft())
print(ans[0])

