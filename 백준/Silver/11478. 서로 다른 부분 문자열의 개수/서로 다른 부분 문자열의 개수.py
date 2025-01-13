import sys
a = sys.stdin.readline().strip()
ans = 0
for i in range(1,len(a)+1):
    ans += len(set([a[j:j+i] for j in range(0,len(a)) if j+i <= len(a)]))
print(ans)