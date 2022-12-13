def solution(emergency):
    dic = {}
    answer = []
    a = sorted(emergency,reverse=True)
    for i in range(len(a)):
        dic[a[i]] = i+1
    for i in emergency:
        answer.append(dic[i])
    return answer