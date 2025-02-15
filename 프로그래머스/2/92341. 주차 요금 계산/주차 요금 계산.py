from datetime import datetime 
import math
def solution(fees, records):
    
    dic = {}
    trans_time = lambda x: datetime.strptime(x,"%H:%M")
    
    for record in records:
        time, num, action = record.split()
        if dic.get(num,0):
            dic[num].append(time)
        else:
            dic[num] = [time]
        
    ans = []
    for key,val in dic.items():
        if len(val)%2:
            val.append("23:59")
        minute = 0
        for come, out in zip(val[::2], val[1::2]):
            minute += (trans_time(out) - trans_time(come)).total_seconds() / 60
        ans.append((key,minute))
    
    final = []
    for num, total in sorted(ans,key=lambda x: x[0]):
        if total <= fees[0]:
            final.append(fees[1])
        else:
            final.append(fees[1] + math.ceil((total - fees[0])/fees[2]) * fees[3])
    return final


