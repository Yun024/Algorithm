def solution(picture, k):
    return sum([[''.join([j*k for j in i])]*k for i in picture],[])