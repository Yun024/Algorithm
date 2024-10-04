def solution(mats, park):
    ans = 0
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "-1":
                answer = 1
                right,down = len(park[0]) - j-1 , len(park) - i -1 
                while 1:
                    if answer > min(right,down):
                        break
                    square = True
                    for u in range(answer+1):
                        for k in range(answer+1):
                            if park[i+u][j+k] != "-1":
                                square =False
                                break
                    if not square:
                        break 
                    answer +=1  
                ans = max(ans,answer)
        
    return -1 if len([i for i in mats if i <= ans])== 0 else max([i for i in mats if i <= ans])