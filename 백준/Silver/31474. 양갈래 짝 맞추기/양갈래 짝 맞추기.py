import math
n = int(input())

up = math.factorial(n)
down = math.factorial(n//2) * 2**(n//2)
print(up//down)