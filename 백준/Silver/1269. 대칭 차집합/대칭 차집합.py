import sys
input = sys.stdin.readline
input()
a,b = set(map(int,input().split())), set(map(int,input().split()))
print(len(a-b) + len(b-a))
