import sys
input = sys.stdin.readline

t = int(input().strip())
ans,graph = [[] for _ in range(t)],[]

for idx in range(t):
    strings = input().strip()
    graph.append([idx for idx,s in enumerate(strings) if s == "Y"])


ans = []
for idx,g in enumerate(graph):
    temp = set()
    for a in g:
        temp.add(a)
        for b in graph[a]:
            temp.add(b)
    if idx in temp:
        temp.remove(idx)
    ans.append(len(temp))
print(max(ans))