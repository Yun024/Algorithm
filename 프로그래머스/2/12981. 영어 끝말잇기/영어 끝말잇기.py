def solution(n, words):
    dic = {}
    for j,i in enumerate(words):
        if dic.get(i) or (j>0 and words[j-1][-1] != i[0]):
            return [j%n+1,j//n+1]
        else:
            dic[i] = 1
    return [0,0]