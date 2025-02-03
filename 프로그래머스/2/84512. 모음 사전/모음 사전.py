def solution(word):
    from itertools import product
    mo = ["A","E","I","O","U"]
    ans = []
    for i in range(1,6):
        ans.append(list(product(mo,repeat=i)))
    ans = sum(ans,[])
    ans = sorted([''.join(i) for i in ans])
    return ans.index(word)+1