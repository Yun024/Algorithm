def solution(arr, n):
    if len(arr)%2 == 0:
        return [i+n if j%2 != 0 else i for j,i in enumerate(arr)]
    else:
        return [i+n if j%2 == 0 else i for j,i in enumerate(arr)]
            