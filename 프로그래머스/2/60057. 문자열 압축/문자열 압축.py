def solution(s):
    ans = len(s)
    for n in range(1,len(s)//2+1):
        temp = []
        for i in range(0,len(s),n):
            if not temp:
                temp.append(s[i:i+n])
            else:
                if temp[-1][-n:] == s[i:i+n]:
                    temp[-1] += s[i:i+n]
                else:
                    temp.append(s[i:i+n])
        
        temp = [len(str(len(i)//n))+n if len(i)>n else len(i) for i in temp]
        ans = min(sum(temp),ans)
    return ans