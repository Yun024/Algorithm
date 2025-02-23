from collections import deque
def solution(queue1, queue2):
    deque1, deque2 = deque(queue1), deque(queue2)
    sum_val = (sum(deque1) + sum(deque2)) // 2
    sum_deq1, sum_deq2 = sum(deque1), sum(deque2)
    ans = 0 
    for i,j in zip(queue1,queue2):
        if i > sum_val or j > sum_val:
            return -1
    while sum_deq1 != sum_val:
        if sum_deq1 > sum_deq2:
            temp = deque1.popleft()
            sum_deq1 -= temp
            sum_deq2 += temp
            deque2.append(temp)
        else:
            temp = deque2.popleft()
            sum_deq1 += temp
            sum_deq2 -= temp
            deque1.append(temp)
        ans +=1
        if ans > 3* len(queue1):
            return -1
    return ans
    