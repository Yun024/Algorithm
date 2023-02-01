
def solution(t, p):
    answer = 0
    for i in range(len(t)):
        if int(t[i:i+len(p)] ) <= int(p) and len(t[i:i+len(p)]) == len(p) :
            answer +=1
    return answer

# def solution(t,p):
#     return len([int(t[j:j+len(p)]) for j,i in enumerate(t) 
#                 if int(t[j:j+len(p)]) <= int(p) and len(t[j:j+len(p)]) == len(p)])