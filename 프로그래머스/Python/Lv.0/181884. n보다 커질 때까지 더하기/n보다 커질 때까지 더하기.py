def solution(numbers, n):
    a,b = 0,0
    while a <= n:
        a += numbers[b]
        b += 1
    return a