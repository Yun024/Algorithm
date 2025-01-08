def solution(numbers):
    if not sum(numbers):
        return "0" 
    else:
        return''.join(map(str,sorted(numbers, key=lambda x: (str(x)*4)[:4],reverse=True)))
    