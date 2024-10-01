def solution(friends, gifts):
    
    ln = len(friends)
    dic = {}
    answer = [0] * ln
    
    gift_idx = [0]*ln                       # 선물지수
    gift = [[0] * ln for i in range(ln)]    # 선물 주고받은 횟수
    
    
    # 인덱스대신 사용할 사전 생성
    for j,i in enumerate(friends):          
        dic[i] = j
        
    # 선물 주고받은 횟수 만들기 
    for i in gifts:
        gift[dic[i.split()[0]]][dic[i.split()[1]]] +=1  
    
    # 선물지수 계산
    for i in range(ln):                                 
        sum_col = 0
        for j in gift:
            sum_col += j[i]
        gift_idx[i] += (sum(gift[i]) - sum_col)
    
    for i in range(ln):
        for j in range(ln):
            if gift[i][j] - gift[j][i] > 0 :
                answer[i] +=1
            elif gift[i][j] - gift[j][i] ==0:
                if gift_idx[i] - gift_idx[j] > 0:
                    answer[i] +=1
                
    
    return max(answer)
        
    
    
    