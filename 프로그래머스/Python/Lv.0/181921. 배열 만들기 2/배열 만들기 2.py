def solution(l, r):
    ans =  [i for i in list(range(l,r+1)) if str(i).replace('5','').replace('0','') == '']  
    return ans if ans else [-1]
    