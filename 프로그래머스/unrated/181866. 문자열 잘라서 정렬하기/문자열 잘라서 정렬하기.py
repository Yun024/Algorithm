def solution(a):
    return sorted([i for i in a.split('x') if len(i)!=0])


#sorted(a.strip('x').split('x'))
