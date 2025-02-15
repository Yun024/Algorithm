def rec(s,l,r,c):
    if l>= r:
        return (1,c)
    elif s[l] != s[r]:
        return (0,c)
    else: 
        return rec(s,l+1,r-1,c+1)

def isp(s):
    return print(*rec(s, 0, len(s)-1,1))

n = int(input())
for i in range(n):
    s = input()
    isp(s)