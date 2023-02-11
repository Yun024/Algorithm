def solution(lottos, win_nums):
    zero_len = list(map(str,lottos)).count("0")
    answer = len([i for i in lottos if i in win_nums])
    return [min(7-answer-zero_len,6),min(7-answer,6)]