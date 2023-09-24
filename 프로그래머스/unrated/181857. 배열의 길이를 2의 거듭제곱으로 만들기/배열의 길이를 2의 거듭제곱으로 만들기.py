def solution(arr):
    ans = [1]
    c = 2
    while c<1025:
        ans.append(c)
        c*=2 
    return arr + [0] * min([i - len(arr) for i in ans if i-len(arr) >= 0])
    
    
        
    