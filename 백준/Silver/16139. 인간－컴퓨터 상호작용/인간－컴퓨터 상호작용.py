import sys

def prefix_sum(S,inpt):

    dp = [[0] * 26 for _ in range(len(S))]   
    for j,i in enumerate(S):
        dp[j] = dp[j-1][:]
        dp[j][ord(i)%97] += 1

    ans = []
    for alpha,l,r in inpt:
        
        num = ord(alpha)%97
        if not int(l):
            temp = dp[int(r)][num]
        else:
            temp = dp[int(r)][num] - dp[int(l)-1][num]
        ans.append(temp)

    return ans

input = sys.stdin.readline

S = input().strip()
n = int(input().strip())
inpt = [input().split() for _ in range(n)]
ans = prefix_sum(S,inpt)

for i in ans:
    print(i)
