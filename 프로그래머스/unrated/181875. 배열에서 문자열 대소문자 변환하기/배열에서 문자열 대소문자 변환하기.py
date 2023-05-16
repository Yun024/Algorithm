def solution(strArr):
    return [i.lower() if j%2 ==0 else i.upper() for j,i in enumerate(strArr)]