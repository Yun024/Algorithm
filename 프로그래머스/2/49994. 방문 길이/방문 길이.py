def solution(dirs):
    
    direction = {
        'L':(-1,0),
        'R':(1,0),
        'U':(0,1),
        'D':(0,-1)
    }
    
    start = (0,0)
    visited = set()
    cnt = 0
    for i in dirs:
        x,y = start
        dx,dy = direction[i]
        nx,ny = dx+x, dy+y
        if -6 < nx < 6 and -6 < ny < 6:
            start = (nx,ny)
            if ((x,y),(nx,ny)) not in visited and ((nx,ny),(x,y)) not in visited:
                cnt +=1
                visited.add(((x,y),(nx,ny)))
    return cnt