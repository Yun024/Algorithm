import sys

input = sys.stdin.readline
n = int(input().strip())

meeting = [list(map(int,input().split())) for _ in range(n)]
sort_meeting = sorted(meeting,key=lambda x: [x[0],x[1]])

a,b = sort_meeting[0]
ans = 1

for i in sort_meeting[1:]:
    c,d = i

    if a <= c and d < b:
        a,b = c,d
    
    elif b <= c:
        a,b = c,d
        ans += 1

print(ans)