def solution(num, total):
    lst = []
    num_sum = 0
    for i in range(num):
        num_sum += i
        lst.append(i)
    return list(map(lambda x: x+(total-num_sum)/num,lst))