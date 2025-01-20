import sys
m,n = map(int,sys.stdin.readline().split())
def isprime(m,n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2,n+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
                
    return [j for j,i in enumerate(primes) if i and j>=m]

primes = isprime(m,n)
for i in primes:
    print(i)
