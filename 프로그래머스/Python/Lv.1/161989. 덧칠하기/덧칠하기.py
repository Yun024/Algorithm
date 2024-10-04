def solution(n, m, section):
    
    ans = 0 
    while len(section)!= 0:
        for i in range(section[0],min(section[0]+m,n+1)):
            if i == section[0]:
                section = section[1:]
            if len(section) == 0:
                break
        ans +=1
    return ans