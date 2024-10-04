def solution(n):
    
    answer = [[0]*n for i in range(n)]
    spiral = ['right','down','left','up']
    spi = 0
    row,col = 0,0
    
    for m in range(1,n**2+1):
        answer[row][col] = m
        if spiral[spi%4] == 'right':
            if col == n-1 or answer[row][col+1] != 0:
                spi +=1
                row +=1
            else:
                col +=1
        elif spiral[spi%4] == 'down':
            if row == n-1 or answer[row+1][col] != 0:
                spi +=1
                col -=1
            else:
                row +=1
        elif spiral[spi%4] == 'left':
            if col == 0 or answer[row][col-1] != 0:
                spi +=1
                row -=1
            else:
                col -=1 
        elif spiral[spi%4] == 'up':
            if row == 0 or answer[row-1][col] !=0:
                spi +=1
                col +=1 
            else:
                row -=1 
    
    return answer