import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    v,u = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(n):
    graph[i+1].sort(reverse=True)

def bfs(start): 
    visited[start] = 1
    cnt = 2
    q = deque()
    q.append(start)

    while q:
        node = q.popleft()

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = cnt
                cnt +=1
                q.append(next_node)

bfs(r)
for i in range(1,n+1):
    print(visited[i])