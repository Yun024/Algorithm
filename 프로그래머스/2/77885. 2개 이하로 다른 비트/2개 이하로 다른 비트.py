def f(n):
    ans = list(bin(n).replace('b',''))
    for i in range(len(ans)-1,-1,-1):
        if ans[i] == '0':
            ans[i] = '1'
            ans[i+1] = '0'
            break
    return int(''.join(ans),2)

def solution(numbers):
    return [f(n) if n%2==1 else n+1 for n in numbers]