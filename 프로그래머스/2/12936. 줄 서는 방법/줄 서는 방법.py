from itertools import permutations
def solution(n, k):
    k -= 1
    num = 1
    nums = [i for i in range(1,n+1)]
    ans = []
    for i in range(1,n+1):
        num *= i
    for i in range(n,0,-1):
        num //= i
        ans.append(nums.pop(k//num))
        k %= num
        print(k,num)
    return ans
        