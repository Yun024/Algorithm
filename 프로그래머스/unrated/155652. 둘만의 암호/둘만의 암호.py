from string import ascii_lowercase
def solution(s, skip, index):
    al =  [i for i in ascii_lowercase if i not in skip] * 3
    return ''.join([al[al.index(i)+index] for i in s])
    
        
            