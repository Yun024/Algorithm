import itertools 
def solution(nums):
    get = len(nums)/2
    unique = len(set(nums))
    if get > unique:
        return unique
    return get