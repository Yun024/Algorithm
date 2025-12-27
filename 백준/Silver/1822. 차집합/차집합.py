import sys
input = sys.stdin.readline

a,b = map(int,input().split())
aa = set(map(int,input().split()))
bb = set(map(int,input().split()))

temp = list(aa-bb)
print(len(temp))
print(*sorted(temp))