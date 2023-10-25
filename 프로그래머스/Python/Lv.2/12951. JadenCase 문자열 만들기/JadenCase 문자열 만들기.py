def solution(s):
    return ''.join([i.upper() if s[max(j-1,0)]==" " or j == 0 else i.lower() for j,i in enumerate(s) ])
    