def solution(nums):
    get = len(nums)/2
    unique = len(set(nums))
    if get > unique:
        return unique
    return get

def solution(nums):
    return len(set(nums)) if len(nums)/2 > len(set(nums)) else len(nums)/2
