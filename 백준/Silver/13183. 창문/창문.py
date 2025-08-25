import sys
input = sys.stdin.readline

h,w = map(int,input().split())
down = h*(h+1)/2 * w*(w+1)/2
mod = 1000000007

print((h+2)*(w+2)%mod)