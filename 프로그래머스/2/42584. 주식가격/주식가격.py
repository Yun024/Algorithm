def solution(prices):
    ans = []
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                break
        ans.append(j-i)
    return ans

        
        