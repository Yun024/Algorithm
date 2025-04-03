from collections import deque
def solution(sequence, k):
    
    seq = deque(sequence)
    num = deque([])
    sum_num, idx = 0,0
    idx_arr = deque([])
    answer = []
    
    while seq:
        if k > sum_num:
            num.append(seq.popleft())
            sum_num += num[-1]
            idx_arr.append(idx)
            idx +=1
        elif k == sum_num:
            answer.append([idx_arr[0],idx_arr[-1]])
            num.append(seq.popleft())
            sum_num += num[-1]
            idx_arr.append(idx)
            idx +=1
        else:
            idx_arr.popleft()
            sum_num -= num.popleft()
    
    while num:
        if k == sum_num:
            answer.append([idx_arr[0], idx_arr[-1]])
        idx_arr.popleft()
        sum_num -= num.popleft()  
    
    diff = [i[1] - i[0] for i in answer]
    
    return answer[diff.index(min(diff))]
            
        
            
            
        
    
    