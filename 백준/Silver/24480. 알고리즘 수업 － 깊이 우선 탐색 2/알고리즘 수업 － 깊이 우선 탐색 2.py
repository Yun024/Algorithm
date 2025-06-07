import sys
sys.setrecursionlimit(10**5+10)
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    u,v = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(n+1):
    graph[i].sort(reverse=True)

def dfs(node):
    global cnt
    visited[node] = cnt

    for next_node in graph[node]:
        if not visited[next_node]:
            cnt +=1
            dfs(next_node)

dfs(r)

for i in range(1,n+1):
    print(visited[i])

