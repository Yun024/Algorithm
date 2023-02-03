def solution(N, stages):
    dic = {}
    z = len(stages)
    for i in range(1,N+1):
        if z == 0:
            dic.update({i:0})
        else:
            dic.update({i:stages.count(i)/z})
            z -= stages.count(i)
    return list(map(lambda x: x[0],sorted(dic.items(),key=lambda x: x[1],reverse=True)))


