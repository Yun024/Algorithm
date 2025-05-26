def solution(weights):
    
    dic = {}
    for i in weights:
        if dic.get(i,0) == 0:
            dic[i] = 1
        else:
            dic[i] +=1
    
    max_val = max(dic.values())
    dp = [0] * (max_val)
    for i in range(max_val):
        dp[i] = dp[i-1] + i
    
    ans = 0
    for i in dic.values():
        ans += dp[i-1]
    
    ref = {}
    for j,i in dic.items():
        for n in range(2,5):
            if ref.get(j*n,0) == 0:
                ref[j*n] = i
            else:
                ans += ref[j*n] * i
                ref[j*n] += i
                       
    return ans