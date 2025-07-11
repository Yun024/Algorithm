from itertools import permutations
import numpy as np
def solution(picks, minerals):
    
    stress =  [25 if i =='diamond' else 5 if i =='iron' else 1 for i in minerals]
    picks_trans = [ 
        25 if not i else 5 if i == 1 else 1
        for i,v in enumerate(picks)
        for _ in range(v)
    ]
    temp = int(min(len(picks_trans),np.ceil(len(stress)/5)))
    picks = sorted(picks_trans,reverse=True)[:temp]
    
    answer = 5000
    for pick in set(permutations(picks)):
        pick
        tmp = []
        for num in pick:
            tmp += [num]*5
        ans = 0
        for j,i in zip(tmp,stress):
            ans += np.ceil(i/j)
        answer = min(answer,ans)
        
    return answer