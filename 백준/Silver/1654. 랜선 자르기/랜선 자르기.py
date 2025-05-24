import sys

input = sys.stdin.readline
k,n = map(int,input().split())

nums = [int(input().strip()) for _ in range(k)] 

def binary_serach(n,nums):
    
    start = 1
    end = max(nums)
    result = 0
    
    while start <= end:
        
        mid = (start + end)//2 
        total = sum(x // mid for x in nums)

        if total >= n:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result 

print(binary_serach(n,nums))