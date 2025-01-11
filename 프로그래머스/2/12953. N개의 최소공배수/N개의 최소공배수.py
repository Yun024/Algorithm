def solution(arr):
    arr.sort()
    while len(arr)!=1:
        a,b = arr.pop(),arr.pop()
        top = a*b
        while b!=0:
            a,b = b,a%b
        arr.append(top/a)
    return arr[0]
        
        
             