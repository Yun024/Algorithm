import sys
input = sys.stdin.readline

n,k = map(int,input().split())
scores = list(map(lambda x: int(x)*100//n,input().split()))

ans = []
for score in scores:
    if score <= 4:
        ans.append(1)
    elif score <= 11:
        ans.append(2)
    elif score <= 23:
        ans.append(3)
    elif score <= 40:
        ans.append(4)
    elif score <= 60:
        ans.append(5)
    elif score <= 77:
        ans.append(6)
    elif score <= 89:
        ans.append(7)
    elif score <= 96:
        ans.append(8)
    else:
        ans.append(9)

print(*ans)