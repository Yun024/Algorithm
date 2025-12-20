import sys, heapq
input =  sys.stdin.readline

n = int(input().strip())
nums = [int(input().strip()) for _ in range(n)]

def solve(n,nums):    

    if n == 1:
        return 0
    
    dasom = nums[0]
    ans = 0
    another = [-i for i in nums[1:]]
    heapq.heapify(another)

    while 1:
        temp = heapq.heappop(another)
        if ans + dasom > abs(temp):
            break
        temp += 1
        heapq.heappush(another,temp)
        ans += 1

    return ans

print(solve(n,nums))