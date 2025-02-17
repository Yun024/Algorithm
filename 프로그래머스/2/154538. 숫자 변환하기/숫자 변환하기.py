from collections import deque
def solution(x, y, n):
    a = deque()
    a.append((x,0))
    dupl = {x}
    iters = [n,2,3]
    while a:
        num, cnt  = a.popleft()
        if num < y:
            if num + n not in dupl:
                dupl.add(num+n)
                a.append((num+n, cnt+1))
            if num * 2 not in dupl:
                dupl.add(num*2)
                a.append((num*2, cnt+1))
            if num * 3 not in dupl:
                dupl.add(num*3)
                a.append((num*3, cnt+1))
        elif num == y:
            return cnt
    return -1