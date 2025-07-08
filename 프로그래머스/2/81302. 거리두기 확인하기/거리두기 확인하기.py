def solution(places):
        
    def is_safety(place):
        
        def dfs(x,y,n):
            ans = 1
            
            if n == 2:
                return 1
            
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != "X" :
                    if place[nx][ny] =='P':
                        return 0
                    visited[nx][ny] = 1
                    ans *= dfs(nx,ny,n+1)
                    
            return ans
                
        visited = [[0]*5 for _ in range(5)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for x in range(5):
            for y in range(5):
                if not visited[x][y] and place[x][y] == 'P':
                    visited[x][y] = 1
                    if not dfs(x,y,0):
                        return 0
        return 1
    
    return [is_safety(place) for place in places]
        