# def solution(n):
#     answer = [2]
#     for i in range(3,n+1,2):
#         if len([j for j in answer if i%j==0])==0:
#             answer.append(i)
#     return len(answer)  

    
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

def solution(n):
    num = set(list(range(2,n+1)))
    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)
        


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
            
# def solution(n):
#     answer = []
#     for i in range(2,n+1):
#         if len([j for j in range(2,i) if i%j ==0] )==0:
#             answer.append(i)
#     return answer