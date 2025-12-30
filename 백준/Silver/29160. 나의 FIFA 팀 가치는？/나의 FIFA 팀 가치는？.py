import sys,heapq
input = sys.stdin.readline

def best_value(team,ans):
    for n in range(12):
        if team[n]:
            best = -heapq.heappop(team[n])
            if ans[n] < best:
                heapq.heappush(team[n],-ans[n])
                ans[n] = best
            else:
                heapq.heappush(team[n],-best)
    return team,ans

team = [[] for _ in range(12)]
ans = [0]*12
n,k = map(int,input().split())

for _ in range(n):
    p,w = map(int,input().split())
    heapq.heappush(team[p],-w)
    
for _ in range(k):
    team,ans = best_value(team,ans)
    ans = [i-1 if i else 0 for i in ans]
    team,ans = best_value(team,ans)

print(sum(ans))