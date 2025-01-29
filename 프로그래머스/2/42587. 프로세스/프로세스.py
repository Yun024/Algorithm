from collections import deque

def solution(priorities, location):
    sorting = sorted(priorities)
    queue = deque([(i,j) for j,i in enumerate(priorities)])
    n = 0
    ans = []
    while sorting:
        if sorting[-1] == queue[0][0]:
            sorting.pop()
            ans.append(queue.popleft())
        else:
            queue.append(queue.popleft())
    dic = {i[1]:j+1 for j,i in enumerate(ans)}
    return dic[location]