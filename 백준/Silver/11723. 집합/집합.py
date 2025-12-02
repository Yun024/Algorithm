import sys
input = sys.stdin.readline

m = int(input().strip())
ans = [0]*21
for _ in range(m):
    strings = input().strip()
    if strings == "all":
        ans = [1]*21
    elif strings == "empty":
        ans = [0]*21
    else:
        calcul,num = strings.split()
        num = int(num)
        if calcul == "add":
            ans[num] = 1
        elif calcul == "remove":
            ans[num] = 0
        elif calcul == "check":
            print(1 if ans[num] else 0)
        else:
            ans[num] = not(ans[num])