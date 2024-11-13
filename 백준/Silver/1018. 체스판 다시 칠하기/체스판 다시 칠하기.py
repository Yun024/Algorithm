a,b = map(int,input().split())
answer = []
check = []
for i in range(a):
    answer.append(input())
want = ''.join(["WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"])


for i,d in enumerate(answer):
    if i > a-8 :
        break 
    for j,c in enumerate(d):
        if j > b-8:
            break
        check.append(''.join([''.join([answer[g+i][h+j] for h in range(8)]) for g in range(8)]))
ans = 32
for i in check:
    ans1, ans2 = 0,0
    for j,i in zip(want,i):
        if j==i:
            ans2 +=1
        else:
            ans1 +=1
    ans = min(ans,ans1,ans2)
print(ans)