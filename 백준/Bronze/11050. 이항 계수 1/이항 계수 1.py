from itertools import combinations
a,b = map(int,input().split())
print(len(list(combinations([i for i in range(a)],b))))