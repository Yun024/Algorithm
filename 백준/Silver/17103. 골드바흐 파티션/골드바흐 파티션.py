import sys
input()
num_list = list(map(lambda x: int(x.strip()), sys.stdin.readlines()))
m = max(num_list)
def prime(m):
    is_prime = [True] * (m+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2,m+1):
        if is_prime[i]:
            for j in range(i*i,m+1, i):
                is_prime[j] = False
    return [j for j,i in enumerate(is_prime) if i]
primes = prime(m)
dic_m = {i:1 for i in primes}
for i in num_list:
    ans = 0
    for j in [c for c in primes if c <= i//2 ]:
        if dic_m.get(i-j,0):
            ans +=1
    print(ans)