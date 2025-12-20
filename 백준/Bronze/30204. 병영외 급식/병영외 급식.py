import sys
input =  sys.stdin.readline

n,x = map(int,input().split())
nums = list(map(int,input().split()))
print(1 if not sum(nums)%x else 0)