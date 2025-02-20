n,k = map(int,input().split())
from itertools import permutations
for i in list(permutations(range(1,n+1),k)):
    print(*i)