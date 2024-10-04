def solution(park, routes):
    row = len(park) -1
    col = len(park[0]) -1
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                S = [i,j]
    
    for i in routes:
        a,b = i.split()[0], int(i.split()[1])
        if a =='E' and S[1] +b <= col :
            if all(j != 'X'  for j in  [park[S[0]][S[1]+i] for i in range(1,b+1)]):
                S[1] += b
        elif a =='W' and S[1] - b >= 0 :
            if all(j != 'X'  for j in  [park[S[0]][S[1]-i] for i in range(1,b+1)]):
                S[1] -= b
        elif a =='S' and S[0] + b <= row :
            if all(j != 'X'  for j in  [park[S[0]+i][S[1]] for i in range(1,b+1)]):    
                S[0] += b
        elif a =='N' and S[0] - b >= 0 :
            if all(j != 'X'  for j in  [park[S[0]-i][S[1]] for i in range(1,b+1)]):
                S[0] -= b   
    
    return S

                
        