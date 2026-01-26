import sys, heapq
input = sys.stdin.readline

n,m,k = map(int,input().split())
work = [-int(input().strip()) for _ in range(n)]
heapq.heapify(work)
satisfaction = 0

ans = []
while work:
    today_work = -heapq.heappop(work)
    satisfaction = satisfaction//2 + today_work
    today_work -= m
    if today_work > k:
        heapq.heappush(work,-today_work)
    ans.append(satisfaction)

print(len(ans))
for i in ans:
    print(i)