import math
answer,v = 0,0
u,d,g = map(int,input().split())
print(math.ceil((g - u)/(u-d)) + 1)