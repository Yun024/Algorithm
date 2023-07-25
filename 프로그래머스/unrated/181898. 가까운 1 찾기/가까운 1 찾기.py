def solution(arr, idx):
    return -1 if sum(arr[idx:]) == 0 else arr[idx:].index(1) + idx