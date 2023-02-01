def solution(strings, n):
    answer = list(map(lambda x:x[n],strings))
    a = sorted(answer)
    index = [a.index(i) for i in answer]
    for i in range(len(index)):
        try:
            if index[i]== index[i+1]:            
                index[i+1] = index[i]+1
        except:
            pass
    final = [strings[i] for i in index]
    return sorted(sorted(strings),key=lambda x: x[n])