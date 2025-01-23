def solution(citations):
    
    big = max(citations)
    for i in range(big,1,-1):
        if i <= len([j for j in citations if j>=i]):
            return i
    return 0