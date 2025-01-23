def solution(citations):
    if sum(citations) ==0:
        return 0
    big = max(citations)
    for i in range(big,1,-1):
        if i <= len([j for j in citations if j>=i]):
            return i
    