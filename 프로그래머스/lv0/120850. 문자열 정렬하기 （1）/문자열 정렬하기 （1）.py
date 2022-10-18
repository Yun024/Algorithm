def solution(my_string):
    answer= list()
    for i in my_string:
        if i in str(list(range(0,10))):
            answer.append(int(i))
    return sorted(answer)