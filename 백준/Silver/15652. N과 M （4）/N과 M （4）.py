def backtrack(n,m,ans=[]):
    if len(ans) == m:
        print(*ans)
        return 

    for i in range(1,n+1):
        if not ans:
            ans.append(i)
            backtrack(n,m,ans)
            ans.pop()
        elif i >= ans[-1]:
            ans.append(i)
            backtrack(n,m,ans)
            ans.pop()
    

n, m = map(int,input().split())
backtrack(n,m)
