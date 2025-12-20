import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int,sys.stdin.readline().split()))

odd = len([i for i in nums if i%2])
even = n - odd

if n%2 and odd == even+1:
    print(1) 
elif not(n%2) and odd == even:
    print(1)
else:
    print(0)
