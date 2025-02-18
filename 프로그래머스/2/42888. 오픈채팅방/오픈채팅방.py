def solution(record):
    dic = {}
    actions = []
    user_id = []
    for i in record:
        info = i.split()
        if info[0] == "Enter":
            actions.append("님이 들어왔습니다.")
            user_id.append(info[1])
            dic[info[1]] = info[2]
        elif info[0] == "Leave":
            actions.append("님이 나갔습니다.")
            user_id.append(info[1])
        else:
            dic[info[1]] = info[2]
    
    user_nick =  [dic[i] for i in user_id]
    
    return [nick + action for nick, action in zip(user_nick, actions)]
    
    
    
#     for key,val in dic.items():
#         user_ids = user_ids.replace(key,val)
        
#     user_nick = user_ids.split(" ")
    
#     return [nick + action for nick, action in zip(user_nick, actions)]
        
        
    
    