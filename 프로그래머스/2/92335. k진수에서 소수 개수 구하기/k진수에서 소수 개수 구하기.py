def is_prime(ans):
    for j in range(2,int(ans**0.5)+1):
        if ans%j == 0:
            return False
    return True      
def trans(n,k):
    ans = ""
    while n:
        ans += str(n%k)
        n = n//k
    return ans[::-1]

def solution(n, k):
    
    a = trans(n,k)
    a.replace("0","b")
    ans = [i for i in a.split("0") if i and i != "1"]
    
    return len([i for i in ans if is_prime(int(i))])
    