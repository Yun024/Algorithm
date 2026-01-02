from itertools import product
def solution(users, emoticons):
    
    brute = []
    for emoticon in emoticons:
        temp = []
        for event in [10,20,30,40]:
            temp.append((emoticon - int(emoticon*0.01*event),event))
        brute.append(temp)
    
    total = list(product(*brute))
    ans = []
    for t in total:
        left,right = 0,0
        for u in users:
            buy = 0
            for price, sale in t:
                if sale >= u[0]:
                    buy += price
            if buy >= u[1]:
                left += 1
            else:
                right += buy
        ans.append((left,right))
    
    res = sorted(ans,key=lambda x: [x[0],x[1]])[-1]
    return res
    