import math
n = int(input())
ans = 1

for i in range(2,n+1,2):
    ans *= i-1
    ans %= 10**9 + 7

print(ans)