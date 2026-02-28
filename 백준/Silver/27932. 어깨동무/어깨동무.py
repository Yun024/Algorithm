import sys
input = sys.stdin.readline

def solve(n,k,hights):

    diff = [0]*n
    left,right,ans = 0,max(hights),0

    if n == 1:
        return 0 

    for i in range(n):
        if not i:
            diff[i] = abs(hights[i] - hights[i+1])
        elif i == n-1:
            diff[i] = abs(hights[i] - hights[i-1])
        else:
            diff[i] = max(abs(hights[i] - hights[i+1]),abs(hights[i] - hights[i-1]))

    while left <= right:
        mid = (left + right) // 2
        if len([i for i in diff if i > mid]) <= k:
            ans = mid
            right = mid -1
        else:
            left = mid +1

    return ans

n,k = map(int,input().split())
hights = list(map(int,input().split()))
print(solve(n,k,hights))