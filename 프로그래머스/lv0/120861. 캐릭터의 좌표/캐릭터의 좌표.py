def solution(keyinput, board):
    [a,b] = [0,0]
    for i in keyinput:
        if i =="left":
            a -=1
        elif i =="right":
            a +=1 
        elif i=="up":
            b +=1
        elif i =="down":
            b -=1
        if abs(a)> board[0]//2:
            if a>0:
                a -=1
            else:
                a +=1
        elif abs(b)>  board[1]//2:
            if b>0:
                b -=1
            else:
                b +=1
    return [a,b]