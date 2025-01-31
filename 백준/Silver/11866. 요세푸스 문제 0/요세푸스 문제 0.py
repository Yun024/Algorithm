from collections import deque
n,k = map(int,input().split())
d_n = deque([i+1 for i in range(n)])
ans = []
while d_n:
    for i in range(k-1):
        d_n.append(d_n.popleft())
    ans.append(str(d_n.popleft()))
print("<" + ', '.join(ans) + ">")