def solution(dartResult):
    # 두번째 풀이(치환 및 리스트, 슬라이싱 사용하여 풀이)
    dartResult = dartResult.replace("10","k")
    ans =  ["10" if i == "k" else i for i in dartResult]
    sdt = ["S","D","T"]
    answer = []
    for j,i in enumerate(ans):
        if i.isdigit():
            answer.append(int(i))
        elif i in sdt:
            answer[-1] = answer[-1] ** (sdt.index(i)+1)
        elif i =="*":
            answer[-2:] = [c*2 for c in answer[-2:]]
        elif i =="#":
            answer[-1] = answer[-1] * -1
    return sum(answer)
    
#     최초 풀이(1,0을 10으로 바꾼 후 앞에서부터 계산 if문 남용)
#     answer = []
#     for i in range(len(dartResult)):
#         if dartResult[i-1:i+1]=="10":
#             answer.pop()
#             answer.append("10")
#         else:
#             answer.append(dartResult[i])
#     ans = []
#     for i in answer:
#         if i.isdigit():
#             ans.append(int(i))
#         elif i == "S":
#             ans[-1] = ans[-1]**1
#         elif i =="D":
#             ans[-1] = ans[-1]**2
#         elif i =="T":
#             ans[-1] = ans[-1]**3
#         elif i =="*":
#             if len(ans) ==1:
#                 ans[-1] = ans[-1]*2
#             else:
#                 ans[-1] = ans[-1]*2
#                 ans[-2] = ans[-2]*2
#         elif i =="#":
#             ans[-1] = ans[-1] * -1
            
#     return sum(ans)
        
            