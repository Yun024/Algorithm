def solution(mylist):
    # ans = []
    # for i in range(len(mylist)-1):
    #     ans.append(abs(mylist[i] - mylist[i+1]))
    # return ans
    
    #zip함수 사용, zip함수는 길이가 짧은쪽기준으로 돌아감
    return [abs(j-i) for j,i in zip(mylist,mylist[1:])]
    


