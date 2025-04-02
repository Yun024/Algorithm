def solution(n):
    ans = [[0] * n for _ in range(n)]
    direction = [(1,0),(0,1),(-1,-1)]
    num,d = 1,0
    x,y = -1,0
    
    for i in range(n,0,-1):
        
        a,b = direction[d%3]
        for _ in range(i):
            x +=a
            y +=b
            ans[x][y] = num
            num +=1
        d += 1
    
    # sum([[j for j in i if j != 0] for i in ans],[])
    return [j for i in ans for j in i if j !=0]
    