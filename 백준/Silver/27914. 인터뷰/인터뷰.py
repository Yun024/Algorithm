import sys,math
input = sys.stdin.readline

n,k,q = map(int,input().split())
grades = list(map(int,input().split()))
questions = list(map(int,input().split()))


dp = [0]*n
temp = 0
if grades[0] != k:
    temp = 1
dp[0] = temp

for i in range(1,n):
    dp[i] = dp[i-1]
    if grades[i] != k:
        temp += 1
        dp[i] += temp
    else:
        temp = 0

for i in questions:
    print(dp[i-1])