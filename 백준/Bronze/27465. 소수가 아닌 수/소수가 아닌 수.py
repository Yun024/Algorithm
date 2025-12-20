import sys

def is_prime(n):
    
    for i in range(2,int(n**0.5)+1):
        if not(n%2):
            return False
        
    return True

n = int(sys.stdin.readline().strip())
if n < 4:
    print(4)
elif n%2:
    print(n+1)
else:
    if is_prime(n+1):
        print(n+2)
    else:
        print(n+1)