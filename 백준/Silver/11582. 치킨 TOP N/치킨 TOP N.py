import sys
input = sys.stdin.readline

n = int(input().strip())
review = list(map(int,input().split()))
k = int(input().strip())

temp = n//k

ans = []
for i in range(k):
    ans += sorted(review[i*temp:i*temp+temp])

print(*ans)
    