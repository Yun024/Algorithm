def solution(my_string, is_prefix):
    return int(is_prefix == my_string[:len(is_prefix)])
    
    #return int(my_string.startswith(is_prefix))
    #return int(is_prefix in [my_string[:i+1] for i in range(len(my_string))] )
