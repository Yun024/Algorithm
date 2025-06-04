from collections import defaultdict
import sys
sys.setrecursionlimit(10**5+10)
def dfs(e,r):
    global num
    v[r-1] = num
    visited[r-1] = "Yes"
    for x in e[r]:
        if visited[x-1] == "No":
            num +=1
            dfs(e,x)

input = sys.stdin.readline
n,m,r = map(int,input().split())

v = {i:0 for i in range(n)}
visited = ["No"] * n

edges = [list(map(int,input().split())) for _ in range(m)]
e = defaultdict(list)
for j,i in edges:
    e[i].append(j)
    e[j].append(i)
for i in e:
    e[i].sort()

num = 1

dfs(e,r)
for i in v.values():
    print(i)