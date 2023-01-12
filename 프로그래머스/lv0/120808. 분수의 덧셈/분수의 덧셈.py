def multp(arr):
    answer= 1
    for i in arr:
        answer *= i
    return answer
def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    final = [[],[]]
    answer = [numer1 * denom/denom1 + numer2 * denom/denom2, denom ]
    if answer[0] == answer[1]:
        return [1, 1]
    else:
        for j,k in enumerate(answer):
            i =1
            while i != k:
                if k/i == int(k/i):
                    final[j].append(i)
                    k = k/i
                    i = 2
                else :
                    i +=1
            final[j].append(i)
        for i in final[0]:
            if i in final[1]:
                final[1].remove(i)
        if multp(final[1]) == answer[1]:
            return answer
        else :
            ans = answer[1]/multp(final[1])
            return list(map(lambda x: x/ans,answer))
    