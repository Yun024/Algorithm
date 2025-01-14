def solution(k, tangerine):
    dic = {}
    for i in tangerine:
        dic[i] = dic.get(i,0) +1 
    cnt = 0
    sort_dic = sorted(dic.values())
    while k > 0:
        k -= sort_dic.pop()
        cnt +=1
        
    return cnt