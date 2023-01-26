def solution(price, money, count):
    answer = money - sum([price*i for i in range(1,count+1)])
    return  0 if answer>0 else abs(answer)