def solution(s):
    # 간단풀이
    x,_x,ans = 0,0,0
    for i in s:
        if x == _x:
            ans +=1 
            a = i 
        if a == i:
            x +=1 
        else:
            _x +=1
    return ans
        
    # 최초풀이
    # x,_x,ans,z = [],[],[],0
    # for j,i in enumerate(s):
    #     if len(x)==0:
    #         x.append(i)
    #     else:
    #         if i in x:
    #             x.append(i)
    #         elif i not in x:
    #             _x.append(i)
    #     if len(x) == len(_x):
    #         ans.append(s[z:j+1])
    #         z = j+1
    #         x,_x = [],[]
    # ans.append(''.join(x + _x))
    # return len([i for i in ans if len(i) !=0])
            
    
    
    
        
    