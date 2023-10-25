def solution(my_string, is_suffix):
    # answer = []
    # for i in range(len(my_string)):
    #     answer.append(my_string[-(i+1):])
    # if is_suffix in answer:
    #     return 1
    # else :
    #     return 0
    
    return 1 if is_suffix in [my_string[-(i+1):] for i in range(len(my_string)) ] else 0