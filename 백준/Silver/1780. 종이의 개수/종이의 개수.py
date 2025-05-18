import sys

n = int(sys.stdin.readline().strip())
paper = list(map(lambda x: x.split(),sys.stdin.read().split("\n")))
m1,zero,p1 = 0,0,0

def daq(row,col,n):

    global m1,zero,p1

    start = paper[row][col]
    for i in range(row,row+n):
        for j in range(col,col+n):
            if paper[i][j] != start:
                divide = n//3
                for x in range(0,3):
                    for y in range(0,3):
                        daq(row+divide*x,col+divide*y,divide)
                return
    
    if start == "-1":
        m1 +=1
    elif start == "1":
        p1 +=1
    else:
        zero +=1

daq(0,0,n)
print(m1,zero,p1,sep="\n")