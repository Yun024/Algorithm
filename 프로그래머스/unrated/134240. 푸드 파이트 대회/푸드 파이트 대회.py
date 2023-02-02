def solution(food):
    answer = ''.join([str(j+1)*(i//2) for j,i in enumerate(food[1:])])
    return answer + "0" + answer[::-1]