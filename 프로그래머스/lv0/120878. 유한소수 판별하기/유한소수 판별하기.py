def solution(a, b):
    if a/b == int(a/b):
        return 1
    else:
        notinf = [2,5]
        num = [b,a]
        final = []
        for i in num:
            j = 2
            ans = []
            while i !=1:
                if i/j == int(i/j):
                    i = i/j
                    ans.append(j)
                    j = 2
                else :
                    j +=1
            final.append(ans)
        for i in final[1]:
            if i in final[0]:
                final[0].remove(i)
        for i in sorted(list(set(final[0])),reverse=True):
            if i not in notinf or sum(sorted(list(set(final[0])),reverse=True))>7:
                return 2 
            else :
                return 1

