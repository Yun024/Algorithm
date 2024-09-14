def solution(players, callings):
    dic = {}
    for j,i in enumerate(players):
        dic[i] = j
    rev_dic = dict(map(reversed,dic.items()))
    for i in callings:
        n = dic[i]
        rev_dic[n-1], rev_dic[n] = rev_dic[n], rev_dic[n-1]
        dic[rev_dic[n-1]],dic[rev_dic[n]] = dic[rev_dic[n]],dic[rev_dic[n-1]]
    
          
    return list(dict(sorted(dic.items(),key = lambda x: x[1])).keys())
    
        
    

        

    