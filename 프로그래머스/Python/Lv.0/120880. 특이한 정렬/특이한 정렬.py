def solution(numlist, n):
    distance = [abs(i-n) for i in numlist]
    answer =  [numlist[distance.index(i)] for i in sorted(distance)]
    unique = [i for i in list(set(answer)) if answer.count(i)>1]
    for i in range(len(answer)):
        if answer[i] in unique and answer[i] > n:
            answer[i] = n - (answer[i] - n)
    unique = [i for i in list(set(answer)) if answer.count(i)>1]            
    for i in unique:
        for j in range(len(answer)):
            if answer[j] == i:
                answer[j] = n*2 - answer[j]
                break
    return answer
   