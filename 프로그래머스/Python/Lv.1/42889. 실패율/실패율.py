### 풀긴 풀었지만 효율성이 떨어짐(마지막줄 sorted도 바꿔줘야함)
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

### 효율성 증가 시킨 방법
def solution(N,stages):
    dic = {}
    info = [0]*(N+2)
    for stage in stages:
        info[stage] +=1
    for i in range(1,N+1):
        numer = info[i]
        denom = sum(info[i:])
        if denom ==0:
            dic.update({i:0})
        else:
            dic.update({i:numer/denom})
    return sorted(dic,key=lambda x: dic[x],reverse=True)
