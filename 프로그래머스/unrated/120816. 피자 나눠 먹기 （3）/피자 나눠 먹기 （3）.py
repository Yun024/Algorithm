def solution(slice, n):
    if n/slice == int(n//slice):
        answer = n//slice
    else :
        answer = n//slice +1 
    return answer