def solution(my_strings, parts):
    return ''.join([i[j[0]:j[1]+1] for j,i in zip(parts,my_strings)])
    