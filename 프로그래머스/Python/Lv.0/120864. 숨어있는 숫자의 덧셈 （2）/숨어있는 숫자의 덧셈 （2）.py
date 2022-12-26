
def solution(my_string): 
    import re
    numbers = re.findall(r"\d+",my_string)
    return sum([int(i) for i in numbers])