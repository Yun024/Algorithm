from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = [i, j, 0]

    q = deque()
    q.append(start)
    directions = [(1,0), (-1,0), (0,-1), (0,1)]
    visited = [[0]*m for _ in range(n)]
    visited[start[0]][start[1]] = 1

    while q:
        x, y, ans = q.popleft()
        
        for dx, dy in directions:
            nx, ny = x, y
            
            # 미끄러지는 방향으로 끝까지 이동
            while True:
                tx, ty = nx + dx, ny + dy
                if 0 <= tx < n and 0 <= ty < m and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break

            if board[nx][ny] == 'G':
                return ans + 1

            if not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny, ans + 1])
                
    return -1
