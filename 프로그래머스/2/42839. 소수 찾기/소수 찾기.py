def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5) +1):
        if n % i == 0:
            return False
    return True


from itertools import permutations
def solution(numbers):
    ans = set()
    for i in range(len(numbers)+1):
        for j in list(permutations(numbers,i)):
            ans.add(int(''.join(j))) if j else 0
    return sum([is_prime(i) for i in ans])
    
    