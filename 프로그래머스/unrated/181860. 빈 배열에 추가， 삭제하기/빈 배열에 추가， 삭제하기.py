def solution(arr, flag):
    answer = []
    for j,i in zip(arr,flag):
        if i:
            [answer.append(j) for u in list(range(j*2))]
        else:
            [answer.pop() for k in list(range(j))]
            
            
    return answer