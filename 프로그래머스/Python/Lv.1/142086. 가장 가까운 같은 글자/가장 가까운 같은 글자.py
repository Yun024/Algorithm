def solution(s):
    answer = []
    ans =[]
    for i in s:
        if i not in answer:
            ans.append(-1)
            answer.append(i)
        else:
            j = 1
            while answer[-j] != i:
                j +=1
            ans.append(j)
            answer.append(i)
    return ans