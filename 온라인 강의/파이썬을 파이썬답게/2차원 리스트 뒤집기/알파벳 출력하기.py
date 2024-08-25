def solution(mylist):
    # ans = []
    # for i in range(len(mylist)):
    #     ANS = []
    #     for j in range(len(mylist)):
    #         ANS.append(mylist[j][i])
    #     ans.append(ANS)            
    # return ans
    
    # 좀더 간결하게
    # ans = [[] for i in range(len(mylist))]
    # for i in range(len(mylist)):
    #     for j in range(len(mylist)):
    #         ans[i].append(mylist[j][i])
    # return ans
    
    # zip과 unpacking사용
    # list(map(list,zip(*mylist)))
    # list(zip(*mylist))
    return [a for a,b,c in zip(mylist)]
    


