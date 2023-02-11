import itertools
# def solution(nums):
#     answer = list(map(lambda x: sum(x),itertools.combinations(nums,3)))
#     return len([i for i in answer if len([j for j in range(2,int(i**0.5)+1) if i%j==0])==0])

### 풀어쓰기
def solution(nums):
    answer = list(map(lambda x: sum(x),itertools.combinations(nums,3)))
    ans =0
    for i in answer:
        if len([j for j in range(2,int(i**0.5)+1) if i%j ==0])==0:
            ans += 1
    return ans
        
            
                
            