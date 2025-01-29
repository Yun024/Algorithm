from collections import deque
import sys
input = sys.stdin.readline
i = int(input().strip())
queue = deque()
for _ in range(i):
    a = input().strip()
    if a[:4] =="push":
        queue.append(int(a.split()[1]))
    elif a=="front":
        print(queue[0]) if queue else print(-1)
    elif a=="back":
        print(queue[-1]) if queue else print(-1)
    elif a=="pop":
        print(queue.popleft()) if queue else print(-1)
    elif a=="empty":
        print(0) if queue else print(1)
    else:
        print(len(queue))
