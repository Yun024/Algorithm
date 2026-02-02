import sys
input = sys.stdin.readline

def dfs(node,res):
   
    if node == b:
        return res
    
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            ans = dfs(next_node,res+1)
            if ans:
                return ans

n = int(input().strip())
a,b = map(int,input().split())
m = int(input().strip())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
visited[a] = 1

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

result = dfs(a,0)
print(result if result else -1)