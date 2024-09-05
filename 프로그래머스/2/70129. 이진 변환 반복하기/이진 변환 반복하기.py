def solution(s):
    c = s.count('0')
    i = 0
    while 1:
        s = s.replace('0','')
        s = bin(len(s))[2:]
        c += s.count('0')
        i +=1
        if s == '1':
            break
    
    return [i,c]
    