import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input().strip())):
    num = int(input().strip())
    if num==0:
        ans.pop()
    else:
        ans.append(num)
print(sum(ans))
    

