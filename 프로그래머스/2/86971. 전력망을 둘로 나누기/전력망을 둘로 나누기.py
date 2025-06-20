def dfs(node,visited,graph):
    
    cnt = 1
    visited[node] = 1
    for next_node in graph[node]:
        if not visited[next_node]:
            cnt += dfs(next_node,visited,graph)
    
    return cnt
    
def solution(n, wires):
    
    m = n-1
    ans = n
    for i in range(m):
        
        visited = [0] * (n+1)
        graph = [[] for _ in range(n+1)]
        s1,s2 = wires[i]
        
        
        for j in range(m):
            if j != i:
                u,v = wires[j]
                graph[u].append(v)
                graph[v].append(u)
        ans = min(ans,abs(dfs(s1,visited,graph) - dfs(s2,visited,graph)))
        
    return ans