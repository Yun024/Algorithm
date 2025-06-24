from itertools import combinations
def solution(orders, course):
    
    orders = [''.join(sorted(order)) for order in orders]
        
    ans = [{} for _ in range(course[-1])]
    
    for order in orders:
        for num in course:
            for comb in list(combinations(order,num)):
                key = ''.join(comb)
                if ans[num-1].get(key,0):
                    ans[num-1][key] +=1
                else:
                    ans[num-1][key] = 1
    
    final = []
    for num in course:
        if ans[num-1]:
            max_num = max(ans[num-1].values())
            for key,value in ans[num-1].items():
                if value != 1 and value == max_num:
                    final.append(key)
                
    return sorted(final)