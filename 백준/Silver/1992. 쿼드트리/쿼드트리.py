import sys

n = int(sys.stdin.readline().strip())
pic = sys.stdin.read().split("\n")
white,black = "1","0"

def quadtree(row,col,n):

    global white, black
    status = 1
    
    for r in range(row,row+n):
        for c in range(col,col+n):
            if not pic[r][c] == white:
                status *= 0
        if not status:
            break
    else:
        return "1"
    
    status = 1
    for r in range(row,row+n):
        for c in range(col,col+n):
            if not pic[r][c] == black:
                status *= 0
        if not status:
            break
    else:
        return "0"

    half = n//2    
    return "(" + quadtree(row,col,half) + quadtree(row,col+half,half) +\
    quadtree(row+half,col,half) + quadtree(row+half,col+half,half) + ")"
    
print(quadtree(0,0,n))