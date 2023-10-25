def solution(keymap, targets):
    dic = {}
    for u in keymap:
        for j,i in enumerate(u):
            if i not in dic:
                dic.update({i:j+1})
            elif i in dic and dic[i]>j+1:
                dic.update({i:j+1})
    answer = []
    for i in targets:
        ans = 0
        for j in i:
            if j in dic:
                ans += dic[j]
            else:
                ans -=1
                break
        answer.append(ans)
    return answer
#     dic = {}
#     for u in keymap:
#         for j,i in enumerate(u):
#             if i not in dic:
#                 dic.update({i:j+1})
#             elif i in dic and dic[i]>j+1:
#                 dic.update({i:j+1})
    
#     return [sum([dic[j] if j in dic else -1  for j in i ]) for i in targets]     
