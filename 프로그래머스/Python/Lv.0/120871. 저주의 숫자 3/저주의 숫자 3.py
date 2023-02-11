
def solution(n):
    answer = 0
    for i in range(n):
        answer +=1
        while answer%3 == 0 or "3" in [i for i in str(answer)]:
            answer +=1
    return answer

# [i for i in range(1,101) if i%3 != 0 if "3" not in [j for j in str(i)]][n-1]
        