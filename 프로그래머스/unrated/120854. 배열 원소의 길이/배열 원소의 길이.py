# def solution(strlist):
#     answer =list()
#     for i in strlist:
#         answer.append(len(i))
#     return answer


def solution(strlist):
    answer=list()
    for i in range(len(strlist)):
        answer.append(len(strlist[i]))
    return answer