def solution(n):
    return sum(list(map(lambda x: x**2,range(0,n+1,2)))) if n%2 == 0 else sum(list(range(1,n+1,2)))
