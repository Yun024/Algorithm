def solution(rank, attendance):
    answer =  sorted([j*i for j,i in zip(rank,attendance) if j*i != 0])
    return 10000 * rank.index(answer[0]) + 100* rank.index(answer[1]) + rank.index(answer[2])