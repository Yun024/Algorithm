
def solution(my_string):
    num = list(map(lambda x: int(x),my_string.split(" ")[::2]))
    operator = my_string.split(" ")[1::2]
    for i in range(len(operator)):
        if i ==0:
            if operator[i] == "+":
                answer = num[i] +num[i+1]
            elif operator[i] == "-":
                answer = num[i] - num[i+1]
        else:
            if operator[i] =="+":
                answer = answer + num[i+1]
            elif operator[i] == "-":
                answer = answer - num[i+1]
    return answer
        
        
    