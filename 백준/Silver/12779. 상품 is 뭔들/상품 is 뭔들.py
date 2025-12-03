import sys,math

a,b = map(int,sys.stdin.readline().split())

left = math.isqrt(b) - math.isqrt(a)
right = b-a
key = math.gcd(left,right)
print(0 if not left else f"{left//key}/{right//key}")