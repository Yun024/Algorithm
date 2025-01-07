def solution(progresses, speeds):
    answer = []
    while progresses:
        progresses = [a+b for a,b in zip(progresses,speeds)]
        cnt = 0
        while progresses and progresses[0] >= 100:
            cnt +=1
            progresses.pop(0)
            speeds.pop(0)
        if cnt:
            answer.append(cnt) 
    return answer