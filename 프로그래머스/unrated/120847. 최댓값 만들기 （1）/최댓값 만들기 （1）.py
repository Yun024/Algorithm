def solution(numbers):
    a = max(numbers)
    numbers.remove(max(numbers))
    b = max(numbers)
    return a*b