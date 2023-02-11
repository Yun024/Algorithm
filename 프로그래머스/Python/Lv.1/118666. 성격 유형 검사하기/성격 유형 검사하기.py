def solution(survey, choices):
    # 복잡한 정답 추출과정 간소화
    dic = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    for j,i in zip(survey,choices):
        if i-4>0:
            dic[j[1]]+= abs(i-4)
        elif i-4<0:
            dic[j[0]] += abs(i-4)
    ans = ["RT","CF","JM","AN"]
    answer = ""
    for i in range(len(ans)):
        if dic[ans[i][0]] >= dic[ans[i][1]]:
            answer += ans[i][0]
        else:
            answer += ans[i][1]
    return answer
    
    
    # 최초 풀이(정답 추출 과정 복잡)
    # dic = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    # for j,i in zip(survey,choices):
    #     if i-4>0:
    #         dic[j[1]] += abs(i-4)
    #     elif i-4<0:
    #         dic[j[0]] += abs(i-4)
    # answer = sorted(dic,key=lambda x: dic[x],reverse=True)
    # return  answer[min(answer.index("T"),answer.index("R"))] + answer[min(answer.index("C"),answer.index("F"))] + answer[min(answer.index("J"),answer.index("M"))] + answer[min(answer.index("A"),answer.index("N"))]