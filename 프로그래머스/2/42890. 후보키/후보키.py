from collections import deque
def solution(relation):

    row, col = len(relation), len(relation[0])
    answer = []

    q = deque()
    q.append(([],-1))
    
    while q:
        temp,n = q.popleft()
        for c in range(n+1,col):
            new_temp = temp + [c]
            proj = [tuple(relation[r][nt] for nt in new_temp) for r in range(row)]
            if len(set(proj)) != row:
                q.append((new_temp,c))
                continue

            if any(set(ans).issubset(set(new_temp)) for ans in answer):
                continue

            answer.append(new_temp)
            
    return len(answer)