def solution(wallpaper):
    answer = []
    min_xy = [0]*2
    max_xy = [0]*2
    num = 1
    for j,i in enumerate(wallpaper):
        for u,k in enumerate(i):
            if k =='#':
                if num==1:
                    min_xy[0],min_xy[1] = j,u
                    max_xy[0],max_xy[1] = j+1,u+1
                    num+=1
                else:
                    min_xy[0],min_xy[1] = min(min_xy[0],j), min(min_xy[1],u)
                    max_xy[0],max_xy[1] = max(max_xy[0],j+1), max(max_xy[1],u+1)
                    
                    
            
    return min_xy+max_xy