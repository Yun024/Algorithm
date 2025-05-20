def solution(storey):
    
    storey_list = list(map(int,str(storey)[::-1])) + [0]
    ans = 0
    
    for i in range(len(storey_list)-1):
        
        if storey_list[i] > 5:
            storey_list[i+1] += 1
            ans += 10 - storey_list[i]
        elif storey_list[i] == 5:
            if storey_list[i+1] >= 5:
                storey_list[i+1] += 1
            ans += 5
        else:
            ans += storey_list[i]
    
    if storey_list[-1]:
        ans += 1
    return ans

    