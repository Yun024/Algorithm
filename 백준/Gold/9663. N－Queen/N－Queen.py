def backtrack(n, start, col, lc, rc):
    if start == n:
        global ans
        ans +=1
        return 
    
    for i in range(n):
        if not col[i] and not lc[start-i] and not rc[start+i] :
            col[i] = True
            lc[start-i] = True
            rc[start+i] = True
            backtrack(n, start+1, col, lc, rc)
            lc[start-i] = False
            rc[start+i] = False
            col[i]= False

n = int(input())
ans,start = 0,0
col = [False] * n
lc,rc = [False] * (2*n), [False] * (2*n)
backtrack(n, start, col, lc, rc)
print(ans)