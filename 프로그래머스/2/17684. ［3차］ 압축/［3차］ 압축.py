def solution(msg):
    dic = {chr(i):j+1 for j,i in enumerate(range(65,91))}
    ans = []
    j,i = 0,1
    while len(msg) >= i:
        if dic.get(msg[j:i],0):
            i +=1
        else:
            ans.append(dic[msg[j:i-1]])
            dic[msg[j:i]]= len(dic) +1
            j,i = i-1,i
    ans.append(dic[msg[j:i]])
    return ans