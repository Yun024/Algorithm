def solution(k, ranges):
    
    collatz = [k]
    while collatz[-1] != 1:
        if not collatz[-1]%2:
            collatz.append(collatz[-1]//2)
        else:
            collatz.append(collatz[-1]*3+1)
    
    length = len(collatz)-1
    dp = [0]* (length)
    for x in range(length):
        x,y = x,collatz[x]
        nx,ny = x+1, collatz[x+1]
        dp[x] = abs((nx-x)*(ny-y)*0.5) + (nx-x)*min(ny,y)
    
    ans = []
    for x,y in ranges:
        x,y = x,length+y
        if x>y: 
            ans.append(-1)
        else:           
            ans.append(sum(dp[x:y]))
        
    return ans