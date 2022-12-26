def solution(i, j, k):
    answer = 0
    for c in range(i,j+1):
        for z in str(c):
            if int(z) == k :
                answer +=1
    return answer 