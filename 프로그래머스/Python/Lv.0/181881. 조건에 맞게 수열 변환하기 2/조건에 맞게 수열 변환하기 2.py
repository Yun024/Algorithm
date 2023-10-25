def solution(arr):
    x = 0
    while 1 :
        ans = list(map(lambda x: x/2 if x >= 50 and x%2 == 0 else x*2+1 if x < 50 and x%2 == 1 else x ,arr))
        if arr == ans :
            return x 
        arr = ans
        x +=1 
