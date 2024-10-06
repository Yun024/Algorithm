def solution(n):
    answer = 0
    for i in range(1,n//2+1):
        ans = 0
        for j in range(i,n//2+2):
            ans +=j
            if ans == n:
                answer +=1
            elif ans > n:
                break
    
    return answer +1