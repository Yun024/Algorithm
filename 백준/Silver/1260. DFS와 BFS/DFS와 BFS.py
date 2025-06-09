import sys
from collections import deque

def dfs(node):

    global cnt
    dfs_ans.append(node)
    dfs_visited[node] = cnt

    for next_node in graph[node]:
        if not dfs_visited[next_node]:
            cnt +=1
            dfs(next_node)

def bfs(start):

    q = deque()
    q.append(start)
    visited = [0] * (n+1)
    visited[start] = 1
    bfs_ans = [start]

    while q:
        node = q.popleft()
        
        for next_node in graph[node]:
            if not visited[next_node]:
                bfs_ans.append(next_node)
                q.append(next_node)
                visited[next_node] = 1

    return bfs_ans

input = sys.stdin.readline
n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v,u = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1,n+1):
    graph[i].sort()

dfs_visited = [0] * (n+1)
cnt = 1
dfs_ans = []

dfs(r)
print(*dfs_ans)
print(*bfs(r))
