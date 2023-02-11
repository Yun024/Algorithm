def solution(array):
    mode = [array.count(i) for i in list(set(array))]

    if mode.count(max(mode))>1:
        return -1
    else:
        return list(set(array))[mode.index(max(mode))]
    