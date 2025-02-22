def recursive(arr,start,ln,dic):
    x,y = start[0],start[1]
    if all(all(arr[j][i]==arr[x][y] for i in range(y,y+ln)) for j in range(x,x+ln)) :
        dic[str(arr[x][y])] +=1
        return
    else:
        next = ln // 2
        for i in range(x,x+ln,next):
            for j in range(y,y+ln,next):
                recursive(arr,[i,j],next,dic)

def solution(arr):
    dic = {'0':0, '1':0}
    recursive(arr,[0,0],len(arr),dic)
    return list(dic.values())