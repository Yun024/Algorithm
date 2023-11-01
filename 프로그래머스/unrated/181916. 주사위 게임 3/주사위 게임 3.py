def solution(a, b, c, d):
    ans =  [[a,b,c,d].count(i) for i in range(1,7) ]
    if 4 in ans:
        return (ans.index(4)+1)*1111
    elif 3 in ans:
        return (10 * (ans.index(3)+1) + (ans.index(1)+1)) **2
    elif len(set([a,b,c,d]))==2   :
        return sum(list(set([a,b,c,d]))) * abs(list(set([a,b,c,d]))[0] - list(set([a,b,c,d]))[1])
    elif len(set([a,b,c,d])) == 4:
        return min(a,b,c,d)
    else:
        return [j+1 for j,i in enumerate(ans) if i ==1][0] *[j+1 for j,i in enumerate(ans) if i ==1][1]
        
        

    
    