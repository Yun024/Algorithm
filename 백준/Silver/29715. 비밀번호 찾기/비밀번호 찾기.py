import sys, math
input = sys.stdin.readline

def action_count(n,m):
    
    ans,num = 1,9
    if m:
        zero,one =0,0
        for _ in range(m):
            a,b = map(int,input().split())
            if not a:
                zero += 1
            else:
                one += 1
            num -=1
        ans *= math.comb(n-one,zero) * math.factorial(zero)
    temp = 1
    for _ in range(n-m):
        temp *= num
        num -=1
    ans *= temp
    return ans

def check_time(x,y,ans):

    if not ans%3:
        return ans*x + ans//3*y - y
    else:
        return ans*x + ans//3*y

n,m = map(int,input().split())
x,y = map(int,input().split())

ans = action_count(n,m)
print(check_time(x,y,ans))