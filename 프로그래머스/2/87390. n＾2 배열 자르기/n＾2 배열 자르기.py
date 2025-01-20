def solution(n, left, right):
    return [max(i%n, i//n)+1 for i in range(n**2)[left:right+1]]
    
    