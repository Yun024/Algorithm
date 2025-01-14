import sys
input = sys.stdin.readline
nums = int(input().strip())

for num in range(nums):
    a,b = map(int,input().split())
    ans = a*b
    while a != 0:
        b,a = a, b%a
    print(ans//b)