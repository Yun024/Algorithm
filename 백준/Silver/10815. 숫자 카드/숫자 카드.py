import sys
input = sys.stdin.readline
input()
a = set(map(int,input().split()))
input()
b = list(map(int,input().split()))
c = a & set(b)
dic = {i:1 for i in c}
print(*[dic.get(i,0) for i in b])