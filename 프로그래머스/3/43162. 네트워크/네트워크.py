import sys
sys.setrecursionlimit(10**6)

def solution(n, computers):
    
    def dfs(node):
        visited[node] = 1
        for next_node,val in enumerate(computers[node]):
            if not visited[next_node] and val:
                dfs(next_node)
        return 1
    visited = [0] * (n)
    ans = 0
    for idx1,val1 in enumerate(computers):
        for idx2,val2 in enumerate(val1):
            if not visited[idx2] and val2:
                ans += dfs(idx2)
    return ans