import sys
input = sys.stdin.readline

n = int(input().strip())
for i in range(1,n+1):
    s = input().strip()
    print(f"Case #{i}: {' '.join(s.split()[::-1])}")