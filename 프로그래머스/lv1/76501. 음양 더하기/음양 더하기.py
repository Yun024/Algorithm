def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if absolutes[i] * signs[i] == 0:
            answer -= absolutes[i]
        else:
            answer += absolutes[i]
    return answer

# def solution(absolutes, signs):
#     return sum([absolutes[j] if i else -absolutes[j] for j,i in enumerate(signs)])

# def solution(absolutes,sings):
#     return sum([j if i else -j for j,i in zip(absolutes,sings)])
