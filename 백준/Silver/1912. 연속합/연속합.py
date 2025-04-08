def seq_num(n,num_list):
    dp = [0 for i in range(n)]
    dp[0] = num_list[0]
    answer = num_list[0]
    
    for i in range(1,n):
        dp[i] = max(num_list[i], dp[i-1] + num_list[i])
        answer = max(answer,dp[i])

    return answer

import sys
input = sys.stdin.readline
n = int(input().strip())
num_list = list(map(int,input().split()))

print(seq_num(n,num_list))