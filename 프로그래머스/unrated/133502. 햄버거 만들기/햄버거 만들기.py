def solution(ingredient):
    # 최종풀이
    ans = []
    answer = 0
    for i in ingredient:
        ans.append(i)
        if ans[-4:] == [1,2,3,1]:
            for j in range(4):
                ans.pop()
            answer+=1
    return answer
        
    # 시간초과풀이
    # ans = ""
    # answer =0
    # for i in ingredient:
    #     ans+=str(i)
    #     if "1231" in ans:
    #         ans = ans[:-4]
    #         answer +=1
    # return answer
    
    # 최초풀이
    # ans = 0
    # answer = []
    # for i in ingredient:
    #     answer.append(i)
    #     try:
    #         if answer[-4] ==1 and answer[-3]==2 and answer[-2]==3 and answer[-1]==1:
    #             answer.pop()
    #             answer.pop()
    #             answer.pop()
    #             answer.pop()
    #             ans +=1
    #     except: pass
    # return ans