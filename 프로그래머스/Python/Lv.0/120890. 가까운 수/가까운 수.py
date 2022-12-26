def solution(array, n):
    result= []
    array.sort()
    for i in array:
        result.append(abs(i-n)) 
    return array[result.index(min(result))]