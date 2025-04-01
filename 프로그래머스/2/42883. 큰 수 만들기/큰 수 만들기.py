# def solution(number, k):
    
#     answer = []
#     end = len(number) - k
#     k += 1
    
#     while len(answer) < end:
    
#         idx = number.index(max(number[:k]))
#         answer.append(number[idx])
#         number = number[idx+1:]
#         k = len(number) - end + len(answer) + 1
        
#         if len(answer) + len(number) == end:
#             return ''.join(answer) + number
    
#     return ''.join(answer)


def solution(number, k):
    
    answer = []
    end = len(number) - k
    reverse_num = list(reversed(number))   

    while reverse_num :
        now = reverse_num.pop()
        while answer:
            if answer[-1] < now:
                answer.pop()
            else:
                break
            if len(answer) + len(reverse_num) < end:
                return ''.join(answer) + now + ''.join(reverse_num[::-1])
        answer.append(now)
    return ''.join(answer[:end])
    
    
    
    