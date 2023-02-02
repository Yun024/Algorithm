### 최초풀이: 효율성 검사에서 시간초과

# def solution(n):
#     answer = []
#     for i in range(2,n+1):
#         if len([j for j in range(2,i) if i%j ==0] )==0:
#             answer.append(i)
#     return answer

### 두번째풀이: 효율성 검사에서 시간초과/ break 사용

# def solution(n):
#     answer = []
#     for i in range(2,n+1):
#         ans = []
#         for j in range(2,i):
#             if len(ans)>0 or j>(i+1)//2:
#                 break
#             elif i%j==0:
#                 ans.append(j)
#         if len(ans)==0:
#             answer.append(i)
#     return len(answer)

### 세번째풀이: 효율성 검사에서 시간초과/ 2의 배수 넘기기 사용

# def solution(n):
#     answer = [2]
#     for i in range(3,n+1,2):
#         if len([j for j in answer if i%j==0])==0:
#             answer.append(i)
#     return len(answer)  

### 네번째풀이: 효율성검사 통과 하지만 느림/ 2의배수 넘기기 및 제곱근전까지 계산 break문 사용 

# def solution(n):
#     answer =[2]
#     for i in range(3,n+1,2):
#         ans = 0 
#         for j in answer:
#             if ans!=0 or j>(i+1)**0.5:
#                 break
#             elif i%j ==0:
#                 ans+=1
#         if ans==0:
#             answer.append(i)
#     return len(answer)

### 최종풀이: 검색을 통해 에라토스테네스의 체 사용 / 가장 효율성이 

def solution(n):
    num = set([2]+list(range(3,n+1,2)))
    
    for i in range(2,int(n**0.5)+1):
        if i in num:
            num -= set(range(i*i,n+1,i))
    return len(num)
