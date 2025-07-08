class Distancechecker:

    def __init__(self,places):
        self.places = places
        self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
    def check_all(self):
        return [self.is_safety(place) for place in self.places]
    
    def is_safety(self,place):
        self.visited = [[0]*5 for _ in range(5)]
        
        for x in range(5):
            for y in range(5):
                if not self.visited[x][y] and place[x][y] == 'P':
                    self.visited[x][y] = 1
                    if not self.dfs(place,x,y,0):
                        return 0
        return 1
    
    def dfs(self,place,x,y,depth):
        if depth == 2:
            return 1
        
        for dx,dy in self.directions:
            nx,ny = x+dx,y+dy
            if 0 <= nx < 5 and 0 <= ny < 5 and not self.visited[nx][ny] and place[nx][ny] != "X":
                if place[nx][ny] == "P":
                    return 0
                self.visited[nx][ny] = 1
                if not self.dfs(place,nx,ny,depth+1):
                    return 0
                
        return 1

def solution(places):
    
    checker = Distancechecker(places)
    return checker.check_all()