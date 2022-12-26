def solution(n):
    k = 1 
    answer = []
    while k<n+1:
        if n/k == int(n/k):
            answer.append(k)
            k = k +1
        else: k = k +1
    return answer