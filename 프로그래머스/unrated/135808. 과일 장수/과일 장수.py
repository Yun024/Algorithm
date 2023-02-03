def solution(k, m, score):
    score.sort(reverse=True)
    answer = [score[i:i+m] for i in range(0,len(score),m)]
    return sum([min(i)*m for i in answer if len(i)==m])

    
    
    
        