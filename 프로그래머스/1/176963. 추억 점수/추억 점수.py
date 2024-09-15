def solution(name, yearning, photo):
    dic = dict()
    for j,i in zip(name,yearning):
        dic[j] = i
    return [sum([dic[j] if j in dic else 0 for j in i]) for i in photo]
    
    