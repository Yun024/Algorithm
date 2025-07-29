import sys,math
input = sys.stdin.readline

n,a,b,c = map(int,input().split())
print(math.factorial(n) // (math.factorial(a)*math.factorial(b)*math.factorial(c)))