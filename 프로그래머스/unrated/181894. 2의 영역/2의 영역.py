def solution(arr):
    ans = [j for j,i in enumerate(arr) if i ==2] 
    return arr[ans[0]:ans[-1]+1] if ans else [-1]