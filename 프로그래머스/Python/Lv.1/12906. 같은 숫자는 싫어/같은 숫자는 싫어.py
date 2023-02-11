def solution(arr):
    answer = [arr[0]]
    [answer.append(i) for i in arr if i != answer[-1]]
    return answer
    