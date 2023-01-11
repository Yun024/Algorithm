def solution(quiz):
    answer =[]
    for i in [i.split("=") for i in quiz]:
        if eval(i[0]) == int(i[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer