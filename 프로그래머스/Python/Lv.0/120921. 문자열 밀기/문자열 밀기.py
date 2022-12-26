
def solution(A, B):
    answer =0
    while A!= B:
        A= A[-1]+ A[:len(A)-1]
        answer +=1 
        if answer == len(A):
            answer = -1
            break
    return answer
