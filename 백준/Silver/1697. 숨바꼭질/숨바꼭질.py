import sys
from collections import deque
input = sys.stdin.readline 
n,k = map(int,input().split())

def bfs(n,k):

    if n == k:
        return 0
    if n > k:
        return n-k
    
    visited = set()
    q = deque()
    q.append((n,0))
    visited.add(n)
    direction = [-1,1,2]

    while q:
        t,cnt = q.popleft()
        if t == k:
            return cnt
        
        for i in direction:
            if i == 2:
                nt = t*2
            else:
                nt = t+i
            if 0 < nt <= k+2 and nt not in visited :
                q.append((nt,cnt+1))
                visited.add(nt)

print(bfs(n,k))
    