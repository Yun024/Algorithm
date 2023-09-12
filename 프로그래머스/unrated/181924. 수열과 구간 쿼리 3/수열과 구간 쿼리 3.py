def solution(arr, queries):
    for j,i in queries:
        a,b = arr[j], arr[i] 
        arr[j] = b
        arr[i] = a
    return arr