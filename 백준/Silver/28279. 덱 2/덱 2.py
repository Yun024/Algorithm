from collections import deque
import sys
input = sys.stdin.readline
n = int(input().strip())
ans = deque()
for i in range(n):
    command = input().strip()
    c = int(command[0])
    if c == 1:
        ans.appendleft(command.split()[1])
    elif c == 2:
        ans.append(command.split()[1])
    elif c == 3:
        print(ans.popleft()) if ans else print(-1)
    elif c == 4:
        print(ans.pop()) if ans else print(-1)
    elif c == 5:
        print(len(ans))
    elif c == 6:
        print(0) if ans else print(1)
    elif c == 7:
        print(ans[0]) if ans else print(-1)
    else:
        print(ans[-1]) if ans else print(-1)