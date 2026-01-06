import re
from collections import deque
from itertools import permutations
def solution(expression):
        
    exp_split = re.findall("\d+|[-*+]",expression)
    queue = deque(exp_split)
    
    ans = []
    for permutation in permutations(["*","-","+"]):
        dic = {}
        for i,v in enumerate(permutation):
            dic[v] = i
            
        length = len(exp_split)
        queue = deque(exp_split)
        for num in range(3):  
            temp = []
            while queue:
                q = queue.popleft()
                if dic.get(q,3) == num:
                    left,right = int(temp.pop()), int(queue.popleft())
                    if q == "+":
                        temp.append(left+right)
                    elif q == "*":
                        temp.append(left*right)
                    else:
                        temp.append(left-right)
                else:
                    temp.append(q)    
            queue = deque(temp)
        ans.append(abs(temp[0]))
    
    return max(ans)