import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort()

def dfs(node):
    global cnt
    cnt +=1
    visited[node] = 1
    
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

dfs(1)
print(cnt-1)