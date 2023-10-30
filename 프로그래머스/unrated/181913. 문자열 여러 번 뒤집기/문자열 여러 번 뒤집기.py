def solution(my_string, queries):
    for s,e in queries:
        my_string = [i for i in my_string]
        my_string[s:e+1] = my_string[s:e+1][::-1]
    return ''.join(my_string)

    