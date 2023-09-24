def solution(arr, queries):
    answer =  [[i for j,i in enumerate(arr) if j>= s  and j<=e and i>k] for s,e,k in queries ]
    return [min(i) if i  else  -1 for i in answer]