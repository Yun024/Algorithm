def solution(arr):
    row,col = len(arr) , len(arr[0])
    if row == col : 
        return arr
    elif row> col :
        return [[j for j in i]+ [0]* (row - col) for i in arr]
    else:
        return arr + [[0]* col] * (col - row)
    