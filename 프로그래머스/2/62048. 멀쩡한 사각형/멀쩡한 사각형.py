def solution(w,h):
    a,b = w,h
    while h:
        w,h = h,w%h
    return (a*b) - (a+b) + (w)