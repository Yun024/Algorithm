import sys

nums = list(map(lambda x:int(x.strip()) ,sys.stdin.readlines()))
ans = 0
for num in nums:
    if ans + num > 100:
        if 100 - ans == ans+num -100:
            ans = max(ans,ans+num)
        elif 100 - ans > ans+num -100:
            ans = ans+num
        break
    ans += num
print(ans)