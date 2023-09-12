def solution(my_string, s, e):
    if s==e:
        return my_string
    elif s==0 and len(my_string) == e+1:
        return my_string[::-1]
    elif s==0 :
        return my_string[e-1::-1] + my_string[e:]
    else:
        return my_string[:s] + my_string[e:s-1:-1] + my_string[e+1:]
    