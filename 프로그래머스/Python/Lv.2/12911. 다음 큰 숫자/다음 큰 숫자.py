def solution(n):
    a  = bin(n).split('b')[1] 
    if a.count('0') == 0:
        return int('10' + '1' * (len(a) -1),2)
    c = n+1
    while bin(n).count('1') != bin(c).count('1'):
        c +=1
        
        
        
    return c