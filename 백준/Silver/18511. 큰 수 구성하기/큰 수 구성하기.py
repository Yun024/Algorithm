import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))
ans = 0

def solve(current_num):
    
    global ans
    if current_num > n:
        return
    
    ans = max(ans,current_num)

    for num in nums:
        next_num = current_num*10 + num
        solve(next_num)
    
solve(0)
print(ans)