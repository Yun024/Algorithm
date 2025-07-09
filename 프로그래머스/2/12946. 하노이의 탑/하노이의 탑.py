def solution(n):

    ans = []
    def hanoi(num,start,medium,end):
        
        if num == 1:
            ans.append([start+1,end+1])
            tower[end].append(tower[start].pop())
            return 
        hanoi(num-1,start,end,medium)
        tower[end].append(tower[start].pop())
        ans.append([start+1,end+1])
        hanoi(num-1,medium,start,end)
            
    tower = [[i for i in range(n,0,-1)],[],[]]
    hanoi(len(tower[0]),0,1,2)
    
    return ans