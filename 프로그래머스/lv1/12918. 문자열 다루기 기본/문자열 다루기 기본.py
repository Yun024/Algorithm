def solution(s):
    numlist = [str(i) for i in range(10)]
    cond1 = len(s) == 4
    cond2 = len(s) == 6
    cond3 = ''.join([i for i in s if i in numlist]) == s
    return (cond1 or cond2) and cond3