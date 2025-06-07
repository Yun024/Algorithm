import sys
from collections import deque
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    v,u = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(n+1):
    graph[i].sort()


q = deque()
q.append(r)
visited[r] = cnt
cnt +=1 

while q:
    node = q.popleft()
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = cnt
            cnt +=1
            q.append(next_node)

for i in range(1,n+1):
    print(visited[i])