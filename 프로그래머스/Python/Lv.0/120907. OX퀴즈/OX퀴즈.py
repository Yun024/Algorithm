def solution(quiz):
    answer =[]
    for i in [i.split("=") for i in quiz]:
        if i[0].split(" ")[1] == "-":
            if int(i[0].split(" ")[0]) - int(i[0].split(" ")[2]) == int(i[1]):
                answer.append("O")
            else:
                answer.append("X")
        if i[0].split(" ")[1] == "+":
            if int(i[0].split(" ")[0]) + int(i[0].split(" ")[2]) == int(i[1]):
                answer.append("O")
            else:
                answer.append("X")
    return answer