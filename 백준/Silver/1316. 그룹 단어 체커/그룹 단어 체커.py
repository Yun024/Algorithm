answer = 0
for i in range(int(input())):
    ans = []
    answer +=1 
    for j in input():
        if len(ans) == 0:
            ans.append(j)
        elif j in ans and ans[-1] != j:
            answer -=1 
            break
        else:
            ans.append(j)
print(answer)