def solution(n, memo = {}):
    ans = [0 for i in range(n)]
    ans[0] = 0
    ans[1] = 1
    ans[2] = 2
    
    for i in range(3,n):
        ans[i] = (ans[i-1] + ans[i-2]) % 1000000007
        
    return (ans[-1] + ans[-2]) % 1000000007
