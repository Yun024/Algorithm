import sys
num_list = list(map(lambda x: int(x.strip()),sys.stdin.readlines()))[:-1]
def prime(n):
    isprime = [True]*(n+1)
    isprime[0] = isprime[1] = False
    for i in range(2,n+1):
        if isprime[i]:
            for j in range(i*i,n+1,i):
                isprime[j] = False
    return isprime
n = max(num_list)*2
primes = prime(n)
for i in num_list:
    print(len([i for i in primes[i+1:i*2+1] if i]))
    