def solution(topping):
    from collections import Counter
    
    left_count = set()
    right_count = Counter(topping)
    
    ans = 0
    for i in topping:
        left_count.add(i)
        right_count[i] -=1
        if right_count[i] == 0:
            del right_count[i]
        if len(left_count) == len(right_count):
            ans +=1
    return ans
        