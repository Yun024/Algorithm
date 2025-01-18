import sys
input()
num_list = list(map(lambda x: int(x.strip()), sys.stdin.readlines()))

def isprime(a):
    if a < 2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i ==0:
            return False
    return True

for i in num_list:
    while 1:
        if isprime(i):
            print(i)
            break
        else:
            i +=1
