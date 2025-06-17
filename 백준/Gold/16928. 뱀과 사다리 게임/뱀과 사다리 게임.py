import sys
from collections import deque
input = sys.stdin.readline

def bfs(n,m):

    dic = {}
    for _ in range(n+m):
        a,b = map(int,input().split())
        dic[a] = b

    q = deque()
    q.append((1,0))

    visited = [0] * 101
    while q:
        num, ans =  q.popleft()

        for i in range(1,7):
            next_num = num + i
            if next_num == 100:
                return ans+1
            if next_num < 100 and not visited[next_num]:
                visited[next_num] = 1
                if not dic.get(next_num,0):
                    q.append((next_num,ans+1))
                else:
                    q.append((dic[next_num],ans+1))
    
                

    
n,m = map(int,input().split())
print(bfs(n,m))