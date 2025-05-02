import sys

input = sys.stdin.readline

def max_sum(temp,n,k):
    
    if k == 1:
        return max(temp)
    
    if k == n:
        return sum(temp)
    
    dp = [0] * n
    dp[1] = sum(temp[:k])
    cnt = 2
    
    for i in range(k,n):
        dp[cnt] = dp[cnt-1] + temp[i] - temp[i-k]
        cnt +=1

    return max(dp[1:])

n,k = map(int,input().split())
temp = list(map(lambda x: int(x), input().split()))

print(max_sum(temp,n,k))