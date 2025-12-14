import sys
input = sys.stdin.readline

n = int(input().strip())
candys = list(map(int,input().split()))
ans,temp = 0,[]

for candy in candys:
    if not candy%2:
        ans += candy
    else:
        temp.append(candy)

temp.sort(reverse=True)
if len(temp)%2:
    ans += sum(temp[:-1])
else:
    ans += sum(temp)
print(ans)