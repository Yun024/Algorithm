import sys,heapq
input = sys.stdin.readline
n,m = map(int,input().split())

gift = list(map(lambda x: -int(x),input().split()))
heapq.heapify(gift)
child = list(map(int,input().split()))
ans = 0

for c in child:
    g = -heapq.heappop(gift)
    temp = g - c
    if temp < 0:
        break
    elif temp > 0:
        heapq.heappush(gift,-temp)
else:
    ans = 1

print(ans)    