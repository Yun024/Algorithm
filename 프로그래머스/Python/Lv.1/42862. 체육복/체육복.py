def solution(n, lost, reserve):
    lost.sort(); reserve.sort()
    ans = []
    _reserve =  [i for i in reserve if i not in lost]
    _lost =  [i for i in lost if i not in reserve]
    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)
    return n - len(_lost)
            
    # 최초풀이 반복문 남용으로 인해 복잡함 
    # lost.sort(); reserve.sort()
    # ans = []
    # for i in lost:
    #     if i in reserve:
    #         ans.append(i)
    #         reserve.remove(i)
    # for i in ans:
    #     if i in lost:
    #         lost.remove(i)
    # ans = [] 
    # for i in lost:
    #     if i-1 in reserve:
    #         ans.append(i)
    #         reserve.remove(i-1)
    #     elif i+1 in reserve:
    #         ans.append(i)
    #         reserve.remove(i+1)
    # for i in ans:
    #     if i in lost:
    #         lost.remove(i)
    # return n-len(lost)
            
    