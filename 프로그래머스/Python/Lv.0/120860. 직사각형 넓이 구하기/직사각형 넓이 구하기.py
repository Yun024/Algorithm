def solution(dots):
    answer = sum(dots,[])
    return (max(answer[1::2]) - min(answer[1::2])) * (max(answer[::2]) - min(answer[::2]))