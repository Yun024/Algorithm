def dp(n,step):

    original = step[:]

    step[0] = (1,original[0])

    if n <=2:
        return sum(original)

    if n > 1:
        step[1] = (2,original[0] + original[1])    
    if n > 2:
        score1 = original[0] + original[2]
        score2 = original[1] + original[2]
        if score1 > score2:
            step[2] = (1,score1)
        else:
            step[2] = (2,score2)
    
    for i in range(3,n):
        score1 = step[i-2][1] + original[i]
        score2 = step[i-3][1] + original[i-1] + original[i]

        if score1 > score2:
            step[i] = (1,score1)
        else:
            step[i] = (2,score2)

        
    return step[-1][1]

import sys
n = int(sys.stdin.readline())
step = [int(sys.stdin.readline().strip()) for _ in range(n)]
print(dp(n,step))

