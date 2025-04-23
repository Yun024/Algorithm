def min_cnt(n,num_list):

    sort_list = sorted(num_list,key=lambda x: x[0])
    dp = [1] * n

    for i in range(1,n):
        x,y = sort_list[i]
        for j in range(i):
            c,d = sort_list[j]
            if x > c and y > d:
                dp[i] = max(dp[i],dp[j]+1)

    return n - max(dp)

import sys
input = sys.stdin.readline
n = int(input().strip())
num_list = [list(map(int,input().split())) for _ in range(n)]
print(min_cnt(n,num_list))
