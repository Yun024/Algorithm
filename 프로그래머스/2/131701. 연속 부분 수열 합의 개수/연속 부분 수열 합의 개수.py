def solution(elements):
    length = len(elements)
    elements *=2 
    ans = []
    for i in range(length):
        for j in range(i+1,i+1+length):
            ans.append(sum(elements[i:j]))
    return len(set(ans))
        
    