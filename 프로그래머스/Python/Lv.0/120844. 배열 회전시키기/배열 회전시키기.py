def solution(numbers, direction):
    if direction== "right":
        a = numbers.pop()
        numbers.insert(0,a)
    else :
        a = numbers.pop(0)
        numbers.append(a)
    return numbers