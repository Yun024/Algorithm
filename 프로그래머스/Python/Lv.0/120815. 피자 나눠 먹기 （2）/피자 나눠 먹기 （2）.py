def solution(n):
    i = 1
    while (n*i) % 6 != 0:
        i += 1
    return (n*i)/6