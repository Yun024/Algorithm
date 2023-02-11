def solution(n, m):
    a = min(n,m); b = max(n,m)
    a_div = [a/i for i in range(1,a//2+1) if a%i ==0] + [1]
    b_div = [b/i for i in range(1,b//2+1) if b%i ==0] + [1]
    y = [i for i in a_div if i in b_div][0]
    return [y,n*m/y]
    