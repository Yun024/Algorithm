import sys
input = sys.stdin.readline

n = int(input().strip())
milks = list(map(int,input().split()))
ans,temp = 0,0


for milk in milks:
    if milk == temp%3:
        ans += 1
        temp += 1

print(ans)