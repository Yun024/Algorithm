def solution(cacheSize, cities):
    ans = []
    time = 0
    
    for i in cities:
        i = i.upper()
        if cacheSize == 0:
            return len(cities)*5
        if ans:
            if i in ans:
                ans.remove(i)
                ans.append(i)
                time +=1
            else:
                if len(ans) == cacheSize:
                    ans.pop(0)
                    ans.append(i)
                else:
                    ans.append(i)
                time +=5
        else:            
            ans.append(i)
            time +=5
    return time
                