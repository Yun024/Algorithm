import sys,math
input = sys.stdin.readline

mom = {'a','e','i','o','u'}

n = int(input().strip())
for _ in range(n):
    S = input().strip()
    mom_count = 0
    for m in mom:
        mom_count += S.count(m)
    if not mom_count:
        print(-1)
    elif mom_count == 1:
        print(1)
    else:    
        start = 0
        ans = []
        for i,s in enumerate(S):
            if s in mom:
                if start:
                    ans.append(i-start+1)
                start = i+1
        
        print(math.prod(ans)%(10**9+7))