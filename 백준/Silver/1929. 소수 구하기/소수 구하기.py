def isprime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

import sys
m,n = map(int,sys.stdin.readline().split())
primes = [i for i in range(m,n+1) if isprime(i)]
for i in primes:
    print(i)